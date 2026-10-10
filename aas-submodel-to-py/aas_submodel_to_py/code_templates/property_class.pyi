{# A Property class, whose value may be restricted by the template, see SubmodelCodegen.get_value_constraints #}
{% extends "base_class.pyi" %}

{%- block before_init -%}
{% for name, value in value_constraints.items() %}
{{ name }} = {{ value }}
{% endfor %}
{% endblock %}

{%- block in_init -%}
{% if "ALLOWED_VALUES" in value_constraints %}
if value is not None and value not in self.ALLOWED_VALUES:
    raise ValueError(f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}")
{% endif %}
{% if "ALLOWED_PATTERN" in value_constraints %}
if value is not None and not re.fullmatch(self.ALLOWED_PATTERN, xsd.xsd_repr(value)):
    raise ValueError(f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_PATTERN}")
{% endif %}
{% if "ALLOWED_RANGE" in value_constraints %}
if value is not None and (value < self.ALLOWED_RANGE[0]
                          or self.ALLOWED_RANGE[1] is not None and value > self.ALLOWED_RANGE[1]):
    raise ValueError(f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_RANGE}")
{% endif %}
{% endblock %}
