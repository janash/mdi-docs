MDI Standard
============
{% for command_key, command_value in mdi_standard.commands.items() %}
## `{{ command_key }}` : {{ command_value.description }}

{% if command_value.datatype %}
**Data Type**: `{{ command_value.datatype }}`  
**Quantity**:  `{{ command_value.count }}`
{% endif %}

{{ command_value.doc }}
{% endfor %}