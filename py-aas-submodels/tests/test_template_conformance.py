"""Compare instances of generated submodel classes with the template files they were generated from.

The template file is the ground truth the generator starts from, so comparing instances with it
checks the whole chain: template -> BaSyx reader -> generator -> generated code -> instance ->
serialization, see https://github.com/rwth-iat/aas-submodel-template-to-py/issues/40

For every submodel of a template file and its generated class:
- BaSyx reads the template completely. Elements violating the metamodel (e.g. ModelReferences
  starting with a GlobalReference, AASd-123) are dropped by BaSyx and can't be generated; these
  template defects are reported as expected failures.
- A full instance (all elements, see instance_builder) contains every element of the template as
  read by BaSyx, and nothing else. Its elements have the model type, semantic IDs, value type,
  content type, list attributes, display name, description, category, entity type, data
  specifications, extensions and qualifiers of the template.
- A minimal instance (required arguments only) contains every mandatory element of the template.

Intended differences:
- Instances have kind Instance and no template qualifiers (#37).
- Values aren't compared: templates hold example values.
- Items of lists have no idShort (#23); they are built from the first item of the list in the template.
  Lists without item in the template take items of their typeValueListElement and valueTypeListElement.
- Elements that may occur several times (cardinality ZeroToMany/OneToMany) get an index instead of
  an iteration ending (e.g. Keyword{00} -> Keyword0); lists are always one list (#36). Other elements
  may lose the placeholders {00} and __00__ of their idShort (kept if siblings would collide).

The tests run with the templates in tests/data/published (CC BY 4.0, see the README there), or with
all templates if SUBMODEL_TEMPLATES_DIR is the published directory of a clone of
admin-shell-io/submodel-templates.
"""
import functools
import importlib
import importlib.util
import inspect
import io
import json
import os
import pathlib
import re

import pytest
from basyx.aas import model
from basyx.aas.adapter.json import read_aas_json_file, write_aas_json_file
from basyx.aas.model import datatypes

from instance_builder import build_instance

TESTS_DIR = pathlib.Path(__file__).resolve().parent
TEMPLATES_DIR = pathlib.Path(os.environ.get("SUBMODEL_TEMPLATES_DIR", TESTS_DIR / "data" / "published"))
REGENERATE_SCRIPT = TESTS_DIR.parent / "regenerate_submodels.py"
REGENERATE_WORKFLOW = TESTS_DIR.parents[1] / ".github" / "workflows" / "regenerate-submodels.yml"

CHILDREN = {
    "Submodel": "submodelElements",
    "SubmodelElementCollection": "value",
    "SubmodelElementList": "value",
    "Entity": "statements",
    "AnnotatedRelationshipElement": "annotations",
}
OPERATION_VARIABLES = ("inputVariables", "outputVariables", "inoutputVariables")


def load_regenerate_script():
    spec = importlib.util.spec_from_file_location("regenerate_submodels", REGENERATE_SCRIPT)
    script = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(script)
    return script


def skipped_templates() -> set:
    """Template files the regeneration workflow skips (SKIP_SUBMODELS)"""
    match = re.search(r"SKIP_SUBMODELS: \|\n((?: {8}.+\n)+)", REGENERATE_WORKFLOW.read_text())
    return {line.strip() for line in match.group(1).splitlines()} if match else set()


def template_cases():
    skipped = skipped_templates()
    files = [file for file in sorted(TEMPLATES_DIR.rglob("*.json"))
             if file.relative_to(TEMPLATES_DIR).as_posix() not in skipped]
    module_names = load_regenerate_script().assign_output_names(files, TEMPLATES_DIR)
    for file, module_file in module_names.items():
        module_name = module_file.removesuffix(".py")
        id_shorts = [submodel["idShort"] for submodel in raw_template(file).get("submodels") or []]
        for id_short in id_shorts:
            marks = []
            if id_shorts.count(id_short) > 1:
                marks.append(pytest.mark.xfail(reason="Issue #30: submodels with the same idShort replace each other"))
            yield pytest.param(file, module_name, id_short, marks=marks, id=f"{module_name}.{id_short}")


@functools.lru_cache(maxsize=None)
def raw_template(file: pathlib.Path) -> dict:
    return json.loads(file.read_text(encoding="utf-8-sig"))


@functools.lru_cache(maxsize=None)
def basyx_template(file: pathlib.Path) -> dict:
    """The template as read by BaSyx, which drops elements violating the metamodel"""
    store = read_aas_json_file(io.StringIO(file.read_text(encoding="utf-8-sig")))
    return {submodel.id_short: to_jsonable(submodel) for submodel in store if isinstance(submodel, model.Submodel)}


TEMPLATE_CASES = list(template_cases())


def to_jsonable(submodel: model.Submodel) -> dict:
    output = io.StringIO()
    write_aas_json_file(output, model.DictIdentifiableStore([submodel]))
    return json.loads(output.getvalue())["submodels"][0]


def raw_submodel(file: pathlib.Path, id_short: str) -> dict:
    return next(submodel for submodel in raw_template(file)["submodels"] if submodel["idShort"] == id_short)


def generated_class(module_name: str, id_short: str) -> type:
    """The generated class of the submodel `id_short`, found by its default idShort"""
    try:
        module = importlib.import_module(f"py_aas_submodels.{module_name}")
    except ModuleNotFoundError:
        pytest.skip(f"No module {module_name}: BaSyx reads no submodel from the template")
    classes = [obj for obj in vars(module).values()
               if isinstance(obj, type) and issubclass(obj, model.Submodel) and obj.__module__ == module.__name__
               and inspect.signature(obj).parameters["id_short"].default in (id_short, iteration_stem(id_short))]
    assert classes, f"No class for submodel {id_short} in {module_name}"
    return classes[0]


# Normalization of the compared attributes

def reference(value):
    if not value:
        return None
    return (value.get("type"), tuple((key.get("type"), key.get("value")) for key in value.get("keys", [])),
            reference(value.get("referredSemanticId")))


def lang_strings(value):
    return {text["language"]: text["text"] for text in value or []} or None


def canonical(value):
    return json.dumps(value, sort_keys=True) if value else None


def xsd_value(value_type, lexical):
    """The value of an XSD lexical representation, as BaSyx may write another one (e.g. Z -> +00:00)"""
    try:
        return datatypes.from_xsd(lexical, datatypes.XSD_TYPE_CLASSES[value_type])
    except (KeyError, TypeError, ValueError):
        return lexical


def qualifiers(element: dict):
    """Qualifiers except template qualifiers, which instances don't take over (AASd-119, AASd-129)"""
    return sorted((q.get("type"), q.get("valueType"), str(xsd_value(q.get("valueType"), q.get("value"))),
                   q.get("kind", "ConceptQualifier"), reference(q.get("semanticId")), reference(q.get("valueId")))
                  for q in element.get("qualifiers") or [] if q.get("kind") != "TemplateQualifier") or None


ATTRIBUTES = {
    "modelType": lambda value: value,
    "semanticId": reference,
    "supplementalSemanticIds": lambda value: tuple(reference(r) for r in value or ()) or None,
    "valueType": lambda value: value,
    "typeValueListElement": lambda value: value,
    "valueTypeListElement": lambda value: value,
    "semanticIdListElement": reference,
    "orderRelevant": lambda value: True if value is None else value,
    "displayName": lang_strings,
    "description": lang_strings,
    "category": lambda value: value,
    "entityType": lambda value: value,
    "embeddedDataSpecifications": canonical,
    "extensions": canonical,
}


def cardinality(element: dict):
    for qualifier in element.get("qualifiers") or []:
        if (qualifier.get("type") or "").rsplit("/", 1)[-1].strip().lower() in ("cardinality", "multiplicity"):
            return (qualifier.get("value") or "").strip().lower()
    return None


def takes_several(element: dict) -> bool:
    # Lists are always one list (#36)
    return element["modelType"] != "SubmodelElementList" and (cardinality(element) or "").endswith("tomany")


def is_mandatory(element: dict) -> bool:
    return not (cardinality(element) or "").startswith("zero")


def iteration_stem(id_short: str) -> str:
    """idShort without iteration ending, e.g. "Document{00}", "Document__00__", "Document01" -> "Document" """
    return re.sub(r"(\{\d+\}|__\d+__|_?\d+)$", "", id_short)


def without_placeholder(id_short: str) -> str:
    """idShort without placeholder for numbering, e.g. "Document{00}", "Document__00__" -> "Document" """
    return re.sub(r"(\{\d+\}|__\d+__)$", "", id_short)


def children(element: dict) -> list:
    if element["modelType"] == "Operation":
        return [variable["value"] for key in OPERATION_VARIABLES for variable in element.get(key) or []]
    return element.get(CHILDREN.get(element["modelType"], ""), None) or []


# Comparison

def compare(template: dict, instance: dict, path: str, errors: list, exact_id_shorts: bool = False):
    """Add the differences of `instance` from the element `template` to `errors`. If `exact_id_shorts`,
    the idShorts of children are compared as they are (for comparing a template as read by BaSyx)"""
    for attribute, normalize in ATTRIBUTES.items():
        expected, actual = normalize(template.get(attribute)), normalize(instance.get(attribute))
        if expected != actual:
            errors.append(f"{path}: {attribute} {expected!r} != {actual!r}")
    # Files with an arbitrary content type take it as argument
    if template.get("contentType") not in (None, "", "{arbitrary}") and template.get("contentType") != instance.get("contentType"):
        errors.append(f"{path}: contentType {template.get('contentType')!r} != {instance.get('contentType')!r}")
    if qualifiers(template) != qualifiers(instance):
        errors.append(f"{path}: qualifiers {qualifiers(template)!r} != {qualifiers(instance)!r}")

    if template["modelType"] == "SubmodelElementList":
        compare_list_items(template, instance, path, errors, exact_id_shorts)
        return

    for template_child, instance_children in match_children(children(template), children(instance), path, errors,
                                                            exact_id_shorts):
        if not instance_children:
            errors.append(f"{path}/{template_child.get('idShort')}: missing in the instance")
        for instance_child in instance_children:
            compare(template_child, instance_child, f"{path}/{instance_child.get('idShort')}", errors, exact_id_shorts)


def compare_list_items(template: dict, instance: dict, path: str, errors: list, exact_id_shorts: bool):
    template_items = children(template)
    for n, item in enumerate(children(instance)):
        item_path = f"{path}[{n}]"
        if exact_id_shorts:
            if n < len(template_items):
                compare(template_items[n], item, item_path, errors, exact_id_shorts)
            continue
        if "idShort" in item:
            errors.append(f"{item_path}: list item has idShort {item['idShort']!r}")
        if template_items:
            compare(template_items[0], item, item_path, errors)
        elif (item["modelType"], item.get("valueType")) != (template.get("typeValueListElement"), template.get("valueTypeListElement")):
            errors.append(f"{item_path}: {item['modelType']} {item.get('valueType')} doesn't match the list's "
                          f"{template.get('typeValueListElement')} {template.get('valueTypeListElement')}")
    if exact_id_shorts and len(template_items) != len(children(instance)):
        errors.append(f"{path}: {len(template_items)} items != {len(children(instance))} items")


def match_children(template_children: list, instance_children: list, path: str, errors: list,
                   exact_id_shorts: bool = False) -> list:
    """Return the instance children of each template child. Elements that may occur several times are
    matched by their idShort without iteration ending followed by an index, other elements by their
    idShort with or without placeholder"""
    remaining = list(instance_children)
    matches = []
    for template_child in template_children:
        id_short = template_child.get("idShort") or ""
        if exact_id_shorts:
            matched = [child for child in remaining if child.get("idShort") == id_short]
        elif takes_several(template_child):
            pattern = re.compile(re.escape(iteration_stem(id_short)) + r"\d+")
            matched = [child for child in remaining if pattern.fullmatch(child.get("idShort", ""))]
        else:
            matched = [child for child in remaining if child.get("idShort") in (id_short, without_placeholder(id_short))]
        matched_ids = {id(child) for child in matched}
        remaining = [child for child in remaining if id(child) not in matched_ids]
        matches.append((template_child, matched))
    for child in remaining:
        errors.append(f"{path}/{child.get('idShort')}: not in the template")
    return matches


def missing_mandatory(template: dict, instance: dict, path: str) -> list:
    if template["modelType"] == "SubmodelElementList":
        return []
    errors = []
    for template_child, instance_children in match_children(children(template), children(instance), path, []):
        child_path = f"{path}/{template_child.get('idShort')}"
        if not instance_children:
            if is_mandatory(template_child):
                errors.append(f"{child_path}: mandatory element missing in the minimal instance")
        else:
            errors += missing_mandatory(template_child, instance_children[0], child_path)
    return errors


def report(errors: list) -> str:
    return "\n".join(errors[:40]) + (f"\n... {len(errors) - 40} more" if len(errors) > 40 else "")


def test_templates_found():
    assert TEMPLATE_CASES


@pytest.mark.parametrize("file, module_name, id_short", TEMPLATE_CASES)
def test_basyx_reads_template_completely(file, module_name, id_short):
    template = basyx_template(file).get(id_short)
    if template is None:
        pytest.xfail(f"Template defect: BaSyx reads no submodel {id_short}")

    errors = []
    compare(raw_submodel(file, id_short), template, id_short, errors, exact_id_shorts=True)
    if errors:
        pytest.xfail("Template defect: BaSyx drops or changes elements violating the metamodel:\n" + report(errors))


@pytest.mark.parametrize("file, module_name, id_short", TEMPLATE_CASES)
def test_full_instance_conforms_to_template(file, module_name, id_short):
    cls = generated_class(module_name, id_short)
    template = basyx_template(file)[id_short]
    instance = to_jsonable(build_instance(cls, full=True))

    errors = []
    compare(template, instance, id_short, errors)
    for attribute in ("version", "revision", "templateId"):
        expected, actual = (template.get("administration") or {}).get(attribute), (instance.get("administration") or {}).get(attribute)
        if expected != actual:
            errors.append(f"{id_short}: administration.{attribute} {expected!r} != {actual!r}")
    if instance.get("kind", "Instance") != "Instance":
        errors.append(f"{id_short}: kind {instance['kind']!r}")
    assert errors == [], report(errors)


@pytest.mark.parametrize("file, module_name, id_short", TEMPLATE_CASES)
def test_minimal_instance_has_mandatory_elements(file, module_name, id_short):
    cls = generated_class(module_name, id_short)
    template = basyx_template(file)[id_short]
    instance = to_jsonable(build_instance(cls))

    errors = missing_mandatory(template, instance, id_short)
    assert errors == [], report(errors)
