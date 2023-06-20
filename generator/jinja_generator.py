import inspect
from typing import Union, Iterable, Any

import black
from basyx.aas.adapter.aasx import AASXReader, DictSupplementaryFileContainer
from basyx.aas.model import Property, Referable, Qualifiable, Submodel, \
    SubmodelElement, SubmodelElementCollection, DictObjectStore, MultiLanguageProperty, \
    ReferenceElement, ModelingKind, AbstractObjectStore

from jinja2 import Environment, FileSystemLoader

from generator import util
from generator.util import StringHandler, ReferableHandler, NamingGenerator, \
    get_typehints_for_args


class SubmodelCodegen:

    def __init__(self, templates_dir="code_templates"):
        # Set the directory containing the Jinja templates
        self.env = Environment(loader=FileSystemLoader(templates_dir))

    def generate_from_aasx(self, aasx_file: str, output_file: str = "output.py"):
        obj_store = DictObjectStore()
        file_store = DictSupplementaryFileContainer()

        reader = AASXReader(aasx_file)
        reader.read_into(obj_store, file_store)
        self.generate_from_obj_store(obj_store, output_file)

    def generate_from_obj_store(self, obj_store: AbstractObjectStore,
                                output_file: str = "output.py"):
        result = f"\n{self.generate_imports()}"

        for obj in obj_store:
            if isinstance(obj, Submodel):
                result = f"{result}\n\n{self.generate_specific_cls_for_submodel(obj)}"

        # Format the rendered class using Black
        result = black.format_str(result, mode=black.Mode())

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)

    def generate_imports(self) -> str:
        with open("code_templates/imports.pyi") as f:
            imports = f.read()
        return imports

    def get_se_typehint(self, se, add_raw_val_type=True):
        typehint = NamingGenerator.create_specific_referable_cls_name(se)

        if add_raw_val_type:
            if isinstance(se, Property):
                typehint = f"Union[{StringHandler.reprify(se.value_type)}, {typehint}]"
            elif isinstance(se, MultiLanguageProperty):
                typehint = f"Union[LangStringSet, {typehint}]"
            elif isinstance(se, ReferenceElement):
                typehint = f"Union[Reference, {typehint}]"

        if ReferableHandler.is_iterable(se):
            typehint = f"Iterable[{typehint}]"
        if ReferableHandler.is_optional(se):
            typehint = f"Optional[{typehint}]"
        return typehint

    def generate_specific_cls_for_submodel(self, submodel: Submodel,
                                           template: str = 'submodel_class.pyi') -> str:
        # Define the variables for the template
        render_kwargs = self.default_referable_render_kwargs(
            submodel, exclude_args=["submodel_element"])

        se_as_args = [NamingGenerator.create_arg_name_for_referable(i) for i in submodel]
        for se, arg in zip(submodel, se_as_args):
            render_kwargs["typehints"][arg] = self.get_se_typehint(se)

        embedded_se_classes = "\n\n".join(
            [self.generate_specific_cls_for_se(se) for se in submodel])

        # Render the template with the given variables
        render_kwargs.update(before_init_content=embedded_se_classes,
                             submodel_elements_args=se_as_args)
        return self.render_cls_with_template(template, **render_kwargs)

    def generate_specific_cls_for_se(self, se: SubmodelElement,
                                     template: str = 'base_class.pyi') -> str:
        if isinstance(se, (Property, MultiLanguageProperty, ReferenceElement)):
            return self.generate_specific_cls_for_property_or_reference_element(se)
        elif isinstance(se, SubmodelElementCollection):
            return self.generate_specific_cls_for_se_collection(se)
        else:
            return self.render_cls_with_template(
                template, **self.default_referable_render_kwargs(se))

    def render_cls_with_template(self, template: str, *args: Any, **kwargs: Any):
        template = self.env.get_template(template)
        rendered_class = template.render(*args, **kwargs)
        return rendered_class

    def default_referable_render_kwargs(self, referable: Referable,
                                        exclude_args: Iterable[str] = None,
                                        remove_numeric_ending_from_id_short = True) -> dict:
        exceptions = ["parent"]
        if exclude_args is not None:
            exceptions.extend(exclude_args)
        referable_kwargs = util.get_kwargs_for_init(referable, exceptions=exceptions)

        # set default value of kind to INSTANCE,
        # as initialized objects of generated classes will be mostly instances
        if "kind" in referable_kwargs and referable_kwargs["kind"] is ModelingKind.TEMPLATE:
            referable_kwargs["kind"] = ModelingKind.INSTANCE

        if remove_numeric_ending_from_id_short and hasattr(referable, "id_short"):
            referable_kwargs["id_short"] = util.StringHandler.remove_iteration_ending(referable_kwargs["id_short"])

        # Find and save args with mutable defaults to kwargs_with_mutable_defaults
        # Set defaults of these args to None
        # These args will be handled appropriately in the template
        handle_as_arg_with_mutable_default = ["qualifier"]
        kwargs_with_mutable_defaults = {}
        for arg, default in referable_kwargs.items():
            if util.is_mutable(default) or arg in handle_as_arg_with_mutable_default:
                kwargs_with_mutable_defaults[arg] = default
                referable_kwargs[arg] = None

        typehints = get_typehints_for_args(referable, referable_kwargs.keys())

        return {
            "cls_name": NamingGenerator.create_specific_referable_cls_name(referable),
            "parent_cls_name": StringHandler.reprify(type(referable)),
            "args": [],
            "kwargs": StringHandler.reprify_kwarg_values(referable_kwargs),
            "kwargs_mutable_defaults": StringHandler.reprify_kwarg_values(
                kwargs_with_mutable_defaults),
            "typehints": StringHandler.reprify_kwarg_values(typehints)
        }

    def generate_specific_cls_for_se_collection(self,
                                                se_collection: SubmodelElementCollection,
                                                template: str = 'se_col_class.pyi') -> str:
        # Define the variables for the template
        render_kwargs = self.default_referable_render_kwargs(se_collection,
                                                             exclude_args=["value"])
        # generate arg names for included items of collection
        collection_items = [NamingGenerator.create_arg_name_for_referable(i) for i in
                            se_collection]
        # provide args of included items with typehints
        for se, arg in zip(se_collection, collection_items):
            render_kwargs["typehints"][arg] = self.get_se_typehint(se)

        embedded_se_classes = "\n\n".join(
            [self.generate_specific_cls_for_se(se) for se in se_collection])

        render_kwargs.update(before_init_content=embedded_se_classes,
                             submodel_elements_args=collection_items)
        return self.render_cls_with_template(template, **render_kwargs)

    def generate_specific_cls_for_property_or_reference_element(
            self, property: Union[Property, MultiLanguageProperty],
            template: str = 'base_class.pyi') -> str:
        # Define the variables for the template
        render_kwargs = self.default_referable_render_kwargs(property,
                                                             exclude_args=["value"])
        render_kwargs["args"].insert(0, "value")
        if isinstance(property, Property):
            render_kwargs["typehints"]["value"] = StringHandler.reprify(
                property.value_type)
            render_kwargs["typehints"]["value_type"] = "DataTypeDef"
        elif isinstance(property, MultiLanguageProperty):
            render_kwargs["typehints"]["value"] = "LangStringSet"
        elif isinstance(property, ReferenceElement):
            render_kwargs["typehints"]["value"] = "Reference"

        # Render the template with the given variables
        return self.render_cls_with_template(template, **render_kwargs)


def main():
    codegen = SubmodelCodegen(templates_dir="code_templates")
    aasx_file = "example_data/submodel-templates-main/published/Digital nameplate/2/0/IDTA 02006-2-0_Template_Digital Nameplate_fixed.aasx"
    codegen.generate_from_aasx(aasx_file)
    # with open(aasx_file, encoding="utf8") as aasx_file:
    #    codegen.generate_from_aasx(aasx_file)


main()
