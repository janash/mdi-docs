
"""
Functions to generate pages for MDI Standard
"""

import yaml
from collections import OrderedDict 

def load_standard():
    # Load the MDI standard
    with open("api/mdi_standard/mdi_standard.yaml", "r", encoding='utf-8') as f:
        mdi_standard = yaml.safe_load(f)
    
    mdi_standard = mdi_standard["commands"]

    # Sort the temporary dictionary by its keys and insert into an OrderedDict
    ordered_standard = OrderedDict(sorted(mdi_standard.items()))

    return ordered_standard


def create_page(command_name, command_dict):

    # Create a new page for the command
    page_text = f"# {command_name}\n\n"

    page_text += f"{command_dict['description']}\n"

    if command_dict.get("datatype"):
        page_text += f"\n**Datatype:** `{command_dict['datatype']}`  "
        page_text += f"\n**Quantity**: `{command_dict['count']}`"

    if command_dict.get("format"):
        page_text += f"\n**Format:** `{command_dict['format']}`"

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

    for command, command_info in commands_list.items():

        page_text = create_page(command, command_info)

        with open(f"api/mdi_standard/commands/{command}.md", "w") as f:
            f.write(page_text)