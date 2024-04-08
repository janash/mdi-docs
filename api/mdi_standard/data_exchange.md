# Data Exchange

Commands that allow retrieval of data from the engine or the sending of data to the engine. Each of these commands is used with the `MDI_Send_Command` function.

| Command Name | Description |
|--------------|-------------|
{%- for command_key, command_value in mdi_standard.items() %}
  {%- if command_value.category != "Simulation Control and Node Management" %}
 [`{{- command_key -}}`](commands/{{- command_key -}}) | {{- command_value.description -}} 
  {% endif %}
{%- endfor -%}

<!--Make a TOC for the sidebar and so Sphixnx doesn't complain -->
<!-- These comments are necessary to break up the table and the TOC -->

```{toctree}
:maxdepth: 1
:hidden:

{%- for command_key, command_value in mdi_standard.items() %}
  {%- if command_value.category != "Simulation Control and Node Management" %}
commands/{{- command_key -}}
  {% endif %}
{%- endfor -%}
