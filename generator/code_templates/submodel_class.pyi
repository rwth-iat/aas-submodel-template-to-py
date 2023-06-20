{% extends "referable_with_se_class.pyi" %}

{%- block init_super_args -%}
submodel_element=embedded_submodel_elements,
{{ super() }}
{% endblock %}
