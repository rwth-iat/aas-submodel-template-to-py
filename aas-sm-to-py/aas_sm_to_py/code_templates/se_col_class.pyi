{% extends "referable_with_se_class.pyi" %}

{%- block init_super_args -%}
value=embedded_submodel_elements,
{{ super() }}
{% endblock %}
