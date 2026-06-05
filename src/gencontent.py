import os
import shutil
from markdown_blocks import markdown_to_blocks, markdown_to_html_node


def copy_static():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    recursive_copy("static", "public")

def recursive_copy(source_dir, dest_dir):
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            os.mkdir(dest_path)
            recursive_copy(source_path, dest_path)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block.lstrip("#").strip()
    raise Exception("No Header")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        markdown = file.read()
    with open(template_path) as file:
        template = file.read()
    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()
    title = extract_title(markdown)
    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html_string)
    page = page.replace('href="/', f'href="{basepath}')
    page = page.replace('src="/', f'src="{basepath}')
    directory = os.path.dirname(dest_path)
    if directory != "":
        os.makedirs(directory, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    entries = os.listdir(dir_path_content)
    for entry in entries:
        source_path = os.path.join(dir_path_content, entry)
        next_dest = os.path.join(dest_dir_path, entry)
        if os.path.isdir(source_path):
            os.makedirs(next_dest, exist_ok=True)
            generate_pages_recursive(source_path, template_path, next_dest, basepath)
        elif source_path.endswith(".md"):
            html_dest = next_dest.replace(".md", ".html")
            generate_page(source_path, template_path, html_dest, basepath)
        
