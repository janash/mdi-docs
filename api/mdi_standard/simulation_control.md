# Simulation Control and Node Management 

Commands that influence the flow of the simulation, such as starting or stopping processes, initializing different types of simulations. Each of these commands is used with the `MDI_Send_Command` function.

{% for command_key, command_value in mdi_standard.commands.items() %}

{% if command_value.category == "Simulation Control and Node Management" %}
## `{{ command_key }}` : {{ command_value.description }}

{% if command_value.datatype %}
**Data Type**: `{{ command_value.datatype }}`  
**Quantity**:  `{{ command_value.count }}`
{% endif %}
{% if command_value.format %}
**Format**:  `{{ command_value.format }}`
{% endif %}

{{ command_value.doc }}

{% if command_value.admonition %}
:::{admonition} {{ command_value.admonition.title }}
:class: {{ command_value.admonition.type }}
{{ command_value.admonition.content }}
:::
{% endif %}

{% if command_value.examples %}

::::{tab-set}

:::{tab-item} Python

```python
{{ command_value.examples.python }}
```

:::

:::{tab-item} C++

```cpp
{{ command_value.examples.cpp }}
```

:::

::::

{% endif %}

{% endif %}
{% endfor %}


