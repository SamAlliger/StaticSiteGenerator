import os
import shutil
from markdown_to_html import markdown_to_html_node
from markdown_extraction import extract_title

def main():
    source = os.path.join(".", "static")
    target = os.path.join(".", "public")
    try:
        shutil.rmtree(target)
        os.mkdir(target)
    except:
        raise Exception(f"Couldn't clear directory {target}")
    
    copy_dir(source, target)
    dir_path_content = os.path.join("src", "content")
    template_path = os.path.join(".", "template.html")
    dest_dir_path = os.path.join(".", "public")
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)
    

def copy_dir(source, target):
    source_items = os.listdir(source)
    for item in source_items:
        current_path = os.path.join(source, item)
        current_target = os.path.join(target, item)
        if os.path.isfile(current_path):
            shutil.copy(current_path, target)
        else:
            os.mkdir(current_target)
            copy_dir(current_path, current_target)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    with open(dest_path, "w+") as f:
        f.write(template.replace("{{ Title }}", title).replace("{{ Content }}", content))

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    for content in contents:
        current_path = os.path.join(dir_path_content, content)
        current_target = os.path.join(dest_dir_path, content.replace(".md", ".html"))
        if os.path.isfile(current_path):
            generate_page(current_path, template_path, current_target)
        else:
            os.mkdir(current_target)
            generate_pages_recursive(current_path, template_path, current_target)

main()