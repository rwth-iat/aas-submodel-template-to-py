{# Values of the element (e.g. value) are init arguments, its metadata (e.g. semantic_id) keyword arguments, #}
{# typed by the TypedDict metadata_cls; template_defaults() returns the template's metadata, see #}
{# SubmodelCodegen.default_referable_render_kwargs. Without trailing commas, which would make Black #}
{# put each argument on its own line #}
{%- block class_def -%}
class {{ cls_name }}({{ parent_cls_name }}):
{% endblock %}
    {% filter indent(width=4) %}
    {%- block before_init -%}
    {{ before_init_content }}
    {% endblock %}
    {% endfilter %}
    @staticmethod
    def template_defaults() -> {{ metadata_cls }}:
        return {{ "{" }}{% for key, value in template_defaults.items() %}"{{ key }}": {{ value }}{% if not loop.last %}, {% endif %}{% endfor %}{{ "}" }}

    def __init__(
            self,
            {% filter indent(width=12) %}
            {%- block init_args -%}
            {% for arg in args %}
            {{ arg }}: {{ typehints.get(arg, 'Any') }},
            {% endfor %}
            {% endblock init_args %}
            {%- block init_kwargs -%}
            {% for key, value in kwargs.items() %}
            {{ key }}: {{ typehints.get(key, 'Any') }} = {{ value }},
            {% endfor %}
            {% endblock init_kwargs %}
            {% endfilter %}
            **kwargs: Unpack[{{ metadata_cls }}]
    ):
        {% filter indent(width=8) %}
        {%- block in_init -%}{% endblock %}
        {% endfilter %}
        super().__init__(
            {% filter indent(width=12) %}
            {%- block init_super_args -%}
            {% for arg in args %}
            {{ arg }}={{ arg }},
            {% endfor %}
            {% endblock %}
            {%- block init_super_kwargs -%}
            {% for key in kwargs.keys() %}
            {{ key }}={{ key }},
            {% endfor %}
            {% endblock %}
            {% endfilter %}
            **(self.template_defaults() | kwargs)
        )
    {% filter indent(width=4) %}
    {%- block after_init -%}
    {{ after_init_content }}
    {% endblock %}
    {% endfilter %}
