from markdown_to_htmlnode import markdown_to_htmlnode
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as fp:
        md = fp.read()

    with open(template_path) as fp2:
        template = fp2.read()

    node = markdown_to_htmlnode(md)

    html = node.to_html()

    title = extract_title(md)

    template2 = template.replace("{{ Title }}", title)
    template3 = template2.replace("{{ Content }}", html)
    template4 = template3.replace("href=\"/", f"href=\"{basepath}")
    template5 = template4.replace("src=\"/", f"src=\"{basepath}")
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as fp:
        fp.write(template5)

    return

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    
    if os.path.isfile(dir_path_content):
        new_dest = dest_dir_path.replace(".md", ".html")
        
        generate_page(dir_path_content, template_path, new_dest, basepath)
    else:
        for dir in os.listdir(dir_path_content):
            generate_pages_recursive(dir_path_content + "/" + dir, template_path, dest_dir_path+ "/" + dir, basepath)
    
    return