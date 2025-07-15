from enum import Enum
import re

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and 
                self.text_type == other.text_type and 
                self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            new_nodes.append(node)
            continue

        for i, part in enumerate(parts):
            if part == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes
    
def extract_markdown_images(text):
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = re.split(r"(\!\[.*?\]\(.*?\))", node.text)
        for part in parts:
            if not part:
                continue

            matches = extract_markdown_images(part)
            if matches:
                alt, url = matches[0]
                new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            else:
                new_nodes.append(TextNode(part, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = re.split(r"(\[.*?\]\(.*?\))", node.text)
        for part in parts:
            if not part:
                continue

            matches = extract_markdown_links(part)
            if matches:
                text, url = matches[0]
                new_nodes.append(TextNode(text, TextType.LINK, url))
            else:
                new_nodes.append(TextNode(part, TextType.TEXT))
    return new_nodes

def text_to_textnode(text):
    node = [TextNode(text, TextType.TEXT)]

    new_nodes = split_nodes_image(node)
    new_nodes = split_nodes_link(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)

    return new_nodes

def markdown_to_blocks(markdown):
    blocks = []
    split_markdown = markdown.split("\n")
    current_block = ""

    for line in split_markdown:
        stripped_line = line.strip()
        if stripped_line == "":
            if current_block:
                blocks.append(current_block.strip())
                current_block = ""
        else:
            if current_block:
                current_block += "\n" + stripped_line
            else:
                current_block = stripped_line

    if current_block:
        blocks.append(current_block)

    return blocks