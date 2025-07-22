import re
from blocktype import markdown_to_html_node
import os

def extract_title(markdown):
    header = re.findall("\# (.*?)", markdown)
    if header == []:
        raise Exception("No header found")
    return header[0]

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown_content = f.read()

    with open(template_path, "r") as f:
        template_content = f.read()

    html_node = markdown_to_html_node(markdown_content)
    html = html_node.to_html()
    title = extract_title(markdown_content)

    updated_html = template_content.replace("{{ Title }}", title)
    updated_html = updated_html.replace("{{ Content }}", html)
    updated_html = updated_html.replace('href="/', f'href="{basepath}')
    updated_html = updated_html.replace('src="/', f'src="{basepath}')

    directories = os.path.dirname(dest_path)

    if directories and not os.path.exists(directories):
        os.makedirs(directories)

    with open(dest_path, 'w') as file:
        file.write(updated_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath, root_dir_path_content):
    content_list = os.listdir(dir_path_content)

    for content in content_list:
        full_path = os.path.join(dir_path_content, content)

        rel_path = os.path.relpath(full_path, start=root_dir_path_content)

        dest_path = os.path.join(dest_dir_path, rel_path)

        if os.path.isdir(full_path):
            generate_pages_recursive(full_path, template_path, dest_dir_path, basepath, root_dir_path_content)

        if os.path.isfile(full_path) and full_path.endswith(".md"):
            new_dest_path = dest_path.replace(".md", ".html")
            generate_page(full_path, template_path, new_dest_path, basepath)