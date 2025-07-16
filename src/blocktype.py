from enum import Enum
import re
from htmlnode import HTMLNode
from leafnode import text_node_to_html_node
from textnode import text_to_textnode, TextNode, TextType
from parentnode import ParentNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if(block.startswith("#")):
        matches = re.findall(r"\#{1,6} ", block)
        if matches:
            return BlockType.HEADING

    if(block.startswith("```") and block.endswith("```")):
        return BlockType.CODE
    
    if(block.startswith(">")):
        split_block = block.split("\n")
        for line in split_block:
            if line.startswith(">"):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if(block.startswith("- ")):
        split_block = block.split("\n")
        for line in split_block:
            if line.startswith("- "):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    if(block.startswith("1. ")):
        matches = re.findall(r"\d+\. ", block)
        if matches:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        type = block_to_block_type(block)
        html_node = create_html_node_for_block_type(block, type)
        children.append(html_node)
    return ParentNode("div", children)

def create_html_node_for_block_type(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        text = block.replace("\n", " ")
        children = [text_node_to_html_node(node) for node in text_to_textnode(text)]
        return ParentNode("p", children)
    
    if block_type == BlockType.HEADING:
        length = len(re.match(r"#+",block).group(1))
        children = [text_node_to_html_node(node) for node in text_to_textnode(block)]
        return ParentNode(f"h{length}", children)
    
    if block_type == BlockType.CODE:
        stripped_block = block.strip("`").lstrip()
        node = TextNode(stripped_block, TextType.CODE)
        html_node = text_node_to_html_node(node)
        return ParentNode("pre", [html_node])
    
    if block_type == BlockType.QUOTE:
        fixed_block = re.sub(r"\>", "", block)
        children = [text_node_to_html_node(node) for node in text_to_textnode(fixed_block)]
        return ParentNode("blockquote", children)
    
    if block_type == BlockType.UNORDERED_LIST:
        lines = block.split("\n")
        li_nodes = []
        for line in lines:
            text = re.sub(r"^- ", "", line)
            children = [text_node_to_html_node(node) for node in text_to_textnode(text)]
            li_nodes.append(ParentNode("li", children))
        return ParentNode("ul", li_nodes)
    
    if block_type == BlockType.ORDERED_LIST:
        lines = block.split("\n")
        li_nodes = []
        for line in lines:
            text = re.sub(r"\d+\. ", "", line)
            children = [text_node_to_html_node(node) for node in text_to_textnode(text)]
            li_nodes.append(ParentNode("li", children))
        return ParentNode("ol", li_nodes)