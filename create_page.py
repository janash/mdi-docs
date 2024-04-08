
"""
Functions to generate pages for MDI Standard
"""

import yaml
from collections import OrderedDict
from pathlib import Path 

def load_standard():
    # Load the MDI standard
    with open("api/mdi_standard/mdi_standard.yaml", "r", encoding='utf-8') as f:
        mdi_standard = yaml.safe_load(f)
    return mdi_standard["commands"]

def group_commands(standard):
    """Groups sending and receiving commands together and then sorts them alphabetically"""
    grouped_standard = {}

    for command, command_info in standard.items():
        if command.startswith("<") or command.startswith(">"):
            command_group = command[1:]
        else:   
            command_group = command

        command_info["name"] = command
        
        if command_group not in grouped_standard:
            grouped_standard[command_group] = []
        
        grouped_standard[command_group].append(command_info)

    # Sorting each group's commands alphabetically by their 'name' key
    for group in grouped_standard:
        grouped_standard[group] = sorted(grouped_standard[group], key=lambda x: x['name'])
    
    # Sorting the groups alphabetically and returning an OrderedDict
    ordered_grouped_standard = OrderedDict(sorted(grouped_standard.items()))
    
    return ordered_grouped_standard


def create_page(command_name, command_list):

    # Create a new page for the command
    page_text = f"# {command_name}\n\n"

    for command_dict in command_list:

        page_text += f"\n\n## {command_dict['name']}\n"
        page_text += f"{command_dict['description']}\n"

        if command_dict.get("datatype"):
            page_text += f"\n**Datatype:** `{command_dict['datatype']}`  "
            page_text += f"\n**Quantity**: `{command_dict['count']}`  "

        if command_dict.get("format"):
            page_text += f"\n**Format:** {command_dict['format']}"

        page_text += f"\n\n {command_dict.get('doc')}"

        if command_dict.get("admonition"):
            admonition_info = command_dict["admonition"]

            page_text += f"\n\n:::{{admonition}} {admonition_info['title']}"
            page_text += f"\n:class: {admonition_info['type']}"
            page_text += f"\n\n{admonition_info['content']}"
            page_text += "\n:::"

        if command_dict.get("examples"):
            page_text += "\n\n## Examples\n"

            page_text += "\n\n::::{tab-set}"
            page_text += "\n\n:::{tab-item} Python"
            page_text += "\n\n```python"
            page_text += f"\n{command_dict['examples']['python']}"
            page_text += "\n```\n:::"

            page_text += "\n\n:::{tab-item} C++"
            page_text += "\n\n```cpp"
            page_text += f"\n{command_dict['examples']['cpp']}"
            page_text += "\n```\n:::"

            page_text += "\n\n::::"


    return page_text

def generate_api_pages(app):

    commands_list = load_standard()
    grouped_commands = group_commands(commands_list)
    Path("api/mdi_standard/commands").mkdir(parents=True, exist_ok=True)

    for command, command_list in grouped_commands.items(): 

        page_text = create_page(command, command_list)

        with open(f"api/mdi_standard/commands/{command}.md", "w") as f:
            f.write(page_text)