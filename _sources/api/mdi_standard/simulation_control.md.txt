# Simulation Control and Node Management 

Commands that influence the flow of the simulation, such as starting or stopping processes, initializing different types of simulations. Each of these commands is used with the `MDI_Send_Command` function. 
Click on the function name to view the full documentation for that command.

| Command Name | Description |
|--------------|-------------|
{%- for command_key, command_list in mdi_standard.items() %}
  {%- for command in command_list %}
    {%- if command.category == "Simulation Control and Node Management" %}
  [`{{- command.name -}}`](commands/{{- command_key -}}) | {{- command.description -}} 
    {% endif %}
  {%- endfor %}
{%- endfor -%}

<!--Make a TOC for the sidebar and so Sphinx doesn't complain -->
<!-- These comments are necessary to break up the table and the TOC -->

```{toctree}
:maxdepth: 1
:hidden:

{%- for command_key, command_list in mdi_standard.items() %}
  {%- if command_list[0].category == "Simulation Control and Node Management" %}
commands/{{- command_key -}}
  {% endif %}
{%- endfor -%}