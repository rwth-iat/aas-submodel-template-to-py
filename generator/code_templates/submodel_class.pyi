{% extends "base_class.pyi" %}

{# List se-arguments #}
{%- block init_args -%}
{% for se in submodel_elements_args %}
{% if not typehints.get(se, '').startswith("Optional") %}
{{ se }}: {{ typehints.get(se, 'Any') }},
{% endif %}
{% endfor %}
{{ super() }}
{% endblock %}

{# Set optional se-arguments to None #}
{%- block init_kwargs -%}
{% for se in submodel_elements_args %}
{% if typehints.get(se, '').startswith("Optional") %}
{{ se }}: {{ typehints.get(se, 'Any') }}=None,
{% endif %}
{% endfor %}
{{ super() }}
{% endblock %}

{%- block in_init -%}

{# Check if raw values were passed as se args and build these from raw values if it is the case #}
{# Submodel elements will be built if the corresponding se arg has the following typehint structure: #}
{# Union[raw_type, SpecificSubmodelElementType] or Optional[Union[raw_type, SpecificSubmodelElementType]] #}
{% for se in submodel_elements_args %}
{% set se_typehint = typehints.get(se, '').lstrip("Optional").strip("[]") %}
{% if se_typehint.startswith("Union") %}
{% set types = se_typehint.lstrip("Union").strip("[]").split(",") %}
# Build a submodel element if a raw value was passed in the argument
if isinstance({{ se }}, {{ types[0] }}):
    {{ se }}=self.{{ types[1] }}({{ se }})
{% endif %}
{% endfor %}

embedded_submodel_elements = []
for se_arg in [{% for se in submodel_elements_args -%} {{ se }}{% if not loop.last %},{% endif %}{%- endfor %}]:
    if se_arg is None:
        continue
    elif isinstance(se_arg, SubmodelElement):
        embedded_submodel_elements.append(se_arg)
    elif isinstance(se_arg, Iterable):
        embedded_submodel_elements.extend(se_arg)
    else:
        raise TypeError(f"Unknown type of value in submodel_element_args: {type(se_arg)}")
{% endblock %}

{%- block init_super_args -%}
submodel_element=embedded_submodel_elements,
{{ super() }}
{% endblock %}
