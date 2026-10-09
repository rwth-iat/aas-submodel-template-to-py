{# This template represents a major part of init-method of a referable class, #}
{# such as Submodel or SubmodelElementCollection, which includes submodel elements #}
{% extends "base_class.pyi" %}

{# List arguments in init_args block #}
{# Example output: #}
{# id_: str, #}
{%- block init_args -%}
{{ super() }}
{% for arg_for_se in args_for_submodel_elements %}
    {% if not typehints.get(arg_for_se, '').startswith("Optional") %}
{{ arg_for_se }}: {{ typehints.get(arg_for_se, 'Any') }},
    {% endif %}
{% endfor %}
{% endblock %}

{# Set optional arguments to None in init_kwargs block#}
{# Example output: #}
{# display_name: Optional[LangStringSet] = None, #}
{# category: Optional[str] = None, #}
{# description: Optional[LangStringSet] = None, #}
{%- block init_kwargs -%}
{% for arg_for_se in args_for_submodel_elements %}
    {% if typehints.get(arg_for_se, '').startswith("Optional") %}
{{ arg_for_se }}: {{ typehints.get(arg_for_se, 'Any') }} = None,
    {% endif %}
{% endfor %}
{{ super() }}
{% endblock %}

{%- block in_init -%}

{# Check if raw values were passed in args where SubmodelElements (e.g.Property) are expected #}
{# Build from raw values SubmodelElements (e.g. from 123 build SpecificProperty(value=123))  #}
{# raw_value_builders maps such args to the code building the SubmodelElement from a raw value, #}
{# see SubmodelCodegen.get_raw_value_builder #}
{% set builders = raw_value_builders | default({}) %}
{% for arg_for_se in args_for_submodel_elements %}
    {% set builder = builders.get(arg_for_se) %}

    {% if builder and builder.iterable %}
# Build submodel elements from raw values passed in the argument
if {{ arg_for_se }}:
    {{ arg_for_se }}=[i if isinstance(i, aas.SubmodelElement) else {{ builder.code }} for i in {{ arg_for_se }}]
    {% elif builder %}
# Build a submodel element if a raw value was passed in the argument
if {{ arg_for_se }} and not isinstance({{ arg_for_se }}, aas.SubmodelElement):
    {{ arg_for_se }}={{ builder.code }}
    {% endif %}
{% endfor %}

# Add all passed/initialized submodel elements to a single list
embedded_submodel_elements = []
for se_arg in [{% for se in args_for_submodel_elements -%} {{ se }}{% if not loop.last %},{% endif %}{%- endfor %}]:
    if se_arg is None:
        continue
    elif isinstance(se_arg, aas.SubmodelElement):
        embedded_submodel_elements.append(se_arg)
    elif isinstance(se_arg, Iterable):
        for n, element in enumerate(se_arg):
            element.id_short = f"{element.id_short}{n}"
            embedded_submodel_elements.append(element)
    else:
        raise TypeError(f"Unknown type of value in submodel_element_args: {se_arg.__class__}")
{% endblock %}
