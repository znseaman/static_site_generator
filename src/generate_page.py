import os
from pathlib import Path
import re

from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    first_h1_header_matches = re.findall(r"(^#)\s(.*)", markdown, re.MULTILINE)
    
    if len(first_h1_header_matches[0][0]) == 1:
        return first_h1_header_matches[0][1]
        
    raise Exception(f"This markdown {markdown} does not have a h1 header (#)")

def generate_page(from_path, template_path, dest_path, base_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace("href=\"/", f"href=\"{base_path}")
    template = template.replace("src=\"/", f"src=\"{base_path}")

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)