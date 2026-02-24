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
{# Submodel elements will be built if the corresponding SE arg has the following typehint structure: #}
{# Union[raw_type, SpecificSubmodelElementType] or
    Optional[Union[raw_type, SpecificSubmodelElementType]] or
     Optional[Union[Tuple[raw_type, raw_type], SpecificSubmodelElementType]]] or
      Optional[Iterable[Union[raw_type, SpecificSubmodelElementType]]] or
    #}
{% for arg_for_se in args_for_submodel_elements %}
    {% set se_arg_typehint = typehints.get(arg_for_se, '').lstrip("Optional").strip("[]") %}

    {% if se_arg_typehint.startswith("Union") %}
        {% set types = se_arg_typehint.lstrip("Union").strip("[]").split(",") %}
# Build a submodel element if a raw value was passed in the argument
if {{ arg_for_se }} and not isinstance({{ arg_for_se }}, SubmodelElement):
    {{ arg_for_se }}=self.{{ types[-1] }}({{ arg_for_se }})
    {% elif se_arg_typehint.lstrip("Iterable[").startswith("Union") %}
        {% set types = se_arg_typehint.lstrip("Iterable").strip("[]").lstrip("Union").strip("[]").split(",") %}
# Build a list of submodel elements if a raw values were passed in the argument
if {{ arg_for_se }} and all([isinstance(i, {{ types[0] }}) for i in {{ arg_for_se }}]):
    {{ arg_for_se }}=[self.{{ types[1] }}(i) for i in {{ arg_for_se }}]
    {% endif %}
{% endfor %}

# Add all passed/initialized submodel elements to a single list
embedded_submodel_elements = []
for se_arg in [{% for se in args_for_submodel_elements -%} {{ se }}{% if not loop.last %},{% endif %}{%- endfor %}]:
    if se_arg is None:
        continue
    elif isinstance(se_arg, SubmodelElement):
        embedded_submodel_elements.append(se_arg)
    elif isinstance(se_arg, Iterable):
        for n, element in enumerate(se_arg):
            element.id_short = f"{element.id_short}{n}"
            embedded_submodel_elements.append(element)
    else:
        raise TypeError(f"Unknown type of value in submodel_element_args: {type(se_arg)}")
{% endblock %}
