import re
from blocktype import markdown_to_html_node

def extract_title(markdown):
    header = re.findall("\# (.*?)", markdown)
    if header == None:
        raise Exception("No header found")
    return header.strip("# ")

def generate_page(from_path, template_path, dest_path):

    with open(from_path, "r") as f:
        markdown_content = f.read()

    with open(template_path, "r") as f:
        template_content = f.read()

    html_node = markdown_to_html_node(markdown_content)
    html = html_node.to_html()
    header = extract_title(html)

    