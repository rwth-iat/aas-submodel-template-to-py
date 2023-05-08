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
submodel_elements = [{% for se in submodel_elements_args -%} {{ se }}{% if not loop.last %},{% endif %}{%- endfor %}]
{% endblock %}

{%- block init_super_args -%}
submodel_element=[se for se in submodel_elements if isinstance(se, SubmodelElement)],
{{ super() }}
{% endblock %}
