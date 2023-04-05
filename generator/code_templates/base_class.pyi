{%- block class_def -%}
class {{ custom_aas_cls }}({{ aas_cls }}):
{% endblock %}
    {% filter indent(width=4) %}
        {%- block before_init -%}
{{ before_init_content }}
        {%- endblock -%}
    {%- endfilter %}
    def __init__(
            self,
            {% filter indent(width=12) %}
                {%- block init_args -%}
                    {%- for arg in args %}
{{ arg }}: {{ typehints.get(arg, 'Any') }},
                    {%- endfor %}
                {% endblock init_args %}
                {%- block init_kwargs -%}
                    {%- for key, value in kwargs.items() %}
{{ key }}: {{ typehints.get(key, 'Any') }}={{ value }},
                    {%- endfor %}
                {% endblock init_kwargs %}
            {% endfilter %}
    ):
        {% filter indent(width=8) %}
            {%- block in_init -%}{% endblock %}
        {% endfilter %}
        super().__init__(
            {% filter indent(width=12) %}
                {%- block init_super_args -%}
                    {%- for arg in args %}
                        {{ arg }} = {{ arg }},
                    {%- endfor %}
                {% endblock %}
                {%- block init_super_kwargs -%}
                    {%- for key in kwargs.keys() %}
                        {{ key }} = {{ key }},
                    {%- endfor %}
                {% endblock %}
            {% endfilter %}
        )
    {% filter indent(width=4) %}
        {%- block after_init -%}
            {{ after_init_content }}
        {% endblock %}
    {% endfilter %}
