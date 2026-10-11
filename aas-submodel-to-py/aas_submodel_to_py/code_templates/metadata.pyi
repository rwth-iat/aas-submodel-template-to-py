{# TypedDicts typing the metadata of the BaSyx classes, which generated classes take as keyword arguments, #}
{# see SubmodelCodegen.add_metadata_cls #}
{% for name, (basyx_cls, fields) in metadata_classes.items() %}
class {{ name }}(TypedDict, total=False):
    """Metadata of {{ basyx_cls }}, passed as keyword arguments to its generated classes"""
    {%- for key, typehint in fields.items() %}
    {{ key }}: {{ typehint }}
    {%- endfor %}


{% endfor %}
