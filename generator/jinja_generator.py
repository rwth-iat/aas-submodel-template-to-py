import keyword
from typing import Optional

import black
from basyx.aas.adapter.aasx import AASXReader, DictSupplementaryFileContainer
from basyx.aas.model import Property, Referable, Qualifiable, Submodel, \
    SubmodelElement, SubmodelElementCollection, DictObjectStore

from jinja2 import Environment, FileSystemLoader

from generator import util


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

    def generate_specific_cls_for_submodel(self, submodel: Submodel,
                                           template: str = 'submodel_class.pyi') -> str:
        # Define the variables for the template
        render_kwargs = self.default_referable_render_kwargs(submodel)
        render_kwargs["kwargs"].pop("submodel_element")

        se_as_args = [self.get_referable_arg_name(i) for i in submodel]
        for se, arg in zip(submodel, se_as_args):
            if self.is_optional(se):
                render_kwargs["typehints"][arg] \
                    = f"Optional[{self.get_specific_referable_cls_name(se)}]"
            else:
                render_kwargs["typehints"][arg] = self.get_specific_referable_cls_name(se)

        se_classes_definition = "\n\n".join(
            [self.generate_specific_cls_for_se(se) for se in submodel])

        # Render the template with the given variables
        template = self.env.get_template(template)
        rendered_class = template.render(
            before_init_content=se_classes_definition,
            submodel_elements_args=se_as_args,
            **render_kwargs
        )
        # Print the rendered class
        return rendered_class

    def generate_specific_cls_for_se(self, se: SubmodelElement,
                                     template: str = 'base_class.pyi') -> str:
        if isinstance(se, Property):
            return self.generate_specific_cls_for_property(se)
        elif isinstance(se, SubmodelElementCollection):
            return self.generate_specific_cls_for_se_collection(se)
        else:
            return self._generate_specific_cls_for_se(se, template)

    def _generate_specific_cls_for_se(self, se: SubmodelElement,
                                      template: str = 'base_class.pyi') -> str:
        template = self.env.get_template(template)

        # Define the variables for the template
        # Render the template with the given variables
        rendered_class = template.render(**self.default_referable_render_kwargs(se))
        return rendered_class

    @classmethod
    def get_specific_referable_cls_name(cls, obj: Referable) -> str:
        return util.upper_first(obj.id_short)

    @classmethod
    def get_referable_arg_name(cls, obj: Referable) -> str:
        res = util.lower_first(obj.id_short)
        # check if res is one of python reserved keywords
        if res in keyword.kwlist:
            return f"{res}_"
        return res

    def default_referable_render_kwargs(self, se: SubmodelElement) -> dict:
        return {
            "cls_name": self.get_specific_referable_cls_name(se),
            "parent_cls_name": util.repr_obj(type(se)),
            "args": [],
            "kwargs": util.stringify_kwargs(util.get_kwargs_from(se)),
            "typehints": {}
        }

    def is_optional(self, obj: Qualifiable):
        for q in obj.qualifier:
            if q.type == "Cardinality":
                if q.value in ("ZeroToOne", "ZeroToMany"):
                    return True
                elif q.value in ("One", "OneToMany"):
                    return False
        return None

    def generate_specific_cls_for_se_collection(self,
                                                se_collection: SubmodelElementCollection,
                                                template: str = 'se_col_class.pyi') -> str:
        template = self.env.get_template(template)

        # Define the variables for the template
        render_kwargs = self.default_referable_render_kwargs(se_collection)
        render_kwargs["kwargs"].pop("value")

        se_as_args = [self.get_referable_arg_name(i) for i in se_collection]
        for se, arg in zip(se_collection, se_as_args):
            if self.is_optional(se):
                render_kwargs["typehints"][
                    arg] = f"Optional[{self.get_specific_referable_cls_name(se)}]"
            else:
                render_kwargs["typehints"][arg] = self.get_specific_referable_cls_name(se)

        se_classes_definition = "\n\n".join(
            [self.generate_specific_cls_for_se(se) for se in se_collection])

        # Render the template with the given variables
        rendered_class = template.render(
            before_init_content=se_classes_definition,
            submodel_elements_args=se_as_args,
            **render_kwargs
        )
        return rendered_class

    def generate_specific_cls_for_property(self, property: Property,
                                           template: str = 'base_class.pyi') -> str:
        template = self.env.get_template(template)

        # Define the variables for the template
        render_kwargs = self.default_referable_render_kwargs(property)
        render_kwargs["kwargs"].pop("value")
        render_kwargs["args"].insert(0, "value")
        render_kwargs["typehints"]["value"] = util.repr_obj(property.value_type)

        # Render the template with the given variables
        rendered_class = template.render(**render_kwargs)
        return rendered_class


def main():
    codegen = SubmodelCodegen(templates_dir="code_templates")
    codegen.generate_from_aasx(
        "example_data/DEXPI_package_v2.3.1.aasx")


main()
