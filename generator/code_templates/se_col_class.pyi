{% extends "base_class.pyi" %}

{%- block init_args -%}
{% for se in submodel_elements_args %}
{{ se }}: {{ typehints.get(se, 'Any') }},
{% endfor %}
{{ super() }}
{% endblock %}

{%- block in_init -%}
submodel_elements = [{% for se in submodel_elements_args -%} {{ se }}{% if not loop.last %},{% endif %}{%- endfor %}]
{% endblock %}

{%- block init_super_args -%}
value=[se for se in submodel_elements if isinstance(se, SubmodelElement)],
{{ super() }}
{% endblock %}
