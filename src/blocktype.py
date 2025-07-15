from enum import Enum
import re

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
