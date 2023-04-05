{% extends "base_class.pyi" %}


{%- block in_init -%}
submodel_element = [{% for se in submodel_elements -%} {{ se }}{% if not loop.last %},{% endif %}{%- endfor %}]
{% endblock %}

{%- block init_super_args -%}
submodel_element=[se for se in submodel_element if isinstance(se, SubmodelElement)],
{%- for arg in args %}
{% if arg not in submodel_elements %}{{ arg }} = {{ arg }},{% endif %}
{%- endfor %}
{% endblock %}
