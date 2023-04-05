class {{ custom_aas_cls }}({{ aas_cls }}):
    def __init__(self{% if args or kwargs %},{% endif %}
                 {%- for arg in args %}
                 {{ arg }}: {{ typehints.get(arg, 'Any') }}{% if not loop.last or kwargs %},{% endif %}
                 {%- endfor %}
                 {%- for key, value in kwargs.items() %}
                 {{ key }}: {{ typehints.get(key, 'Any') }}={{ value }}{% if not loop.last %},{% endif %}
                 {%- endfor -%}
                 ):
        super().__init__({%- for arg in args %}
                         {{ arg }} = {{ arg }},
                         {%- endfor %}
                         {%- for key in kwargs.keys() %}
                         {{ key }} = {{ key }},
                         {%- endfor %}
                         )
