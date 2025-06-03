from markdown_to_htmlnode import markdown_to_htmlnode
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as fp:
        md = fp.read()

    with open(template_path) as fp2:
        template = fp2.read()

    node = markdown_to_htmlnode(md)

    html = node.to_html()

    title = extract_title(md)

    template_w_title = template.replace("{{ Title }}", title)
    filled_template = template_w_title.replace("{{ Content }}", html)
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as fp:
        fp.write(filled_template)

    return