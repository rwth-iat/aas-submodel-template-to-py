import inspect
from typing import Union, Iterable, Any

import black
from basyx.aas.adapter.aasx import AASXReader, DictSupplementaryFileContainer
from basyx.aas.model import Property, Referable, Qualifiable, Submodel, \
    SubmodelElement, SubmodelElementCollection, DictObjectStore, MultiLanguageProperty, \
    ReferenceElement

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

        result = f"\n{self.generate_imports()}"

        for obj in obj_store:
            if isinstance(obj, Submodel):
                result = f"{result}\n\n{self.generate_specific_cls_for_submodel(obj)}"

        # Format the rendered class using Black
        result = black.format_str(result, mode=black.Mode())

        with open(output_file, "w") as f:
            f.write(result)

    def generate_imports(self) -> str:
        with open("code_templates/imports.pyi") as f:
            imports = f.read()
        return imports

    def get_se_typehint(self, se):
        typehint = NamingGenerator.create_specific_referable_cls_name(se)
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

        se_classes_definition = "\n\n".join(
            [self.generate_specific_cls_for_se(se) for se in submodel])

        # Render the template with the given variables
        render_kwargs.update(before_init_content=se_classes_definition,
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

    def default_referable_render_kwargs(self, se: SubmodelElement,
                                        exclude_args: Iterable[str] = None) -> dict:
        exceptions = ["parent"]
        if exclude_args is not None:
            exceptions.extend(exclude_args)
        se_kwargs = util.get_kwargs_for_init(se, exceptions=exceptions)

        # Find and save args with mutable defaults to kwargs_with_mutable_defaults
        # Set defaults of these args to None
        # These args will be handled appropriately in the template
        kwargs_with_mutable_defaults = {arg: default for arg, default in
                                        se_kwargs.items() if util.is_mutable(default)}
        for arg in kwargs_with_mutable_defaults:
            se_kwargs[arg] = None

        typehints = get_typehints_for_args(se, se_kwargs.keys())

        return {
            "cls_name": NamingGenerator.create_specific_referable_cls_name(se),
            "parent_cls_name": StringHandler.reprify(type(se)),
            "args": [],
            "kwargs": StringHandler.reprify_kwarg_values(se_kwargs),
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

        se_classes_definition = "\n\n".join(
            [self.generate_specific_cls_for_se(se) for se in se_collection])

        render_kwargs.update(before_init_content=se_classes_definition,
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
    codegen.generate_from_aasx(
        "example_data/DEXPI_package_v2.3.1.aasx")


main()
