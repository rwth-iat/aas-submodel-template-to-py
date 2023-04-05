import os

from basyx.aas.adapter.aasx import DictSupplementaryFileContainer, AASXReader
from basyx.aas.model import DictObjectStore, Submodel
from jinja2 import Environment, FileSystemLoader

from generator import util
from generator.util import repr_obj, strigify_kwargs, upper_first, lower_first


def generate_custom_submodel_cls_from(submodel, env: Environment,
                                      template: str = 'submodel_class.pyi'):
    template = env.get_template(template)

    # Define the variables for the template
    kwargs = strigify_kwargs(util.get_kwargs_from(submodel))
    kwargs.pop("submodel_element")

    typehints = {}
    se_id_shorts = [lower_first(i.id_short) for i in submodel]
    se_as_args = [lower_first(i) for i in se_id_shorts]
    for id_short, arg in zip(se_id_shorts, se_as_args):
        typehints[arg] = upper_first(id_short)

    se_classes_definition = "\n\n".join(
        [generate_custom_se_cls_from(se, env) for se in submodel])

    # Render the template with the given variables
    rendered_class = template.render(
        custom_aas_cls=upper_first(submodel.id_short),
        aas_cls=util.repr_obj(type(submodel)),
        before_init_content=se_classes_definition,
        submodel_elements=se_as_args,
        args=se_as_args,
        kwargs=kwargs,
        typehints=typehints
    )
    # Print the rendered class
    return rendered_class


def generate_custom_se_cls_from(se, env: Environment,
                                template: str = 'base_class.pyi'):
    template = env.get_template(template)

    # Define the variables for the template
    # Render the template with the given variables
    rendered_class = template.render(
        custom_aas_cls=upper_first(se.id_short),
        aas_cls=util.repr_obj(type(se)),
        args=[],
        kwargs=strigify_kwargs(util.get_kwargs_from(se)),
        typehints={"id_short": "str"}
    )
    # Print the rendered class
    return rendered_class


def main():
    obj_store = DictObjectStore()
    file_store = DictSupplementaryFileContainer()

    reader = AASXReader("example_data/IDTA 02006-2-0_Template_Digital Nameplate.aasx")
    reader.read_into(obj_store, file_store)

    # with open("example_data/IDTA 02006-2-0_Template_Digital Nameplate.json", encoding="utf-8") as f:
    # json_deserialization.read_aas_json_file_into(obj_store, f)

    result = ""

    with open("code_templates/imports.jinja") as f:
        imports = f.read()
        result = f"{result}\n{imports}"

    # Set the directory containing the Jinja template
    # Configure Jinja Environment and load the template
    env = Environment(loader=FileSystemLoader("code_templates"))
    for obj in obj_store:
        if isinstance(obj, Submodel):
            result = f"{result}\n\n{generate_custom_submodel_cls_from(obj, env)})"

    with open("output.py", "w") as f:
        f.write(result)


main()
