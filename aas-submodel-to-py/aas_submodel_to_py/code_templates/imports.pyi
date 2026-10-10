{% for module in modules %}
import {{ module }}
{% endfor %}
from typing import {{ typing_imports | join(", ") }}
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd
