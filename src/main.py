from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from copy_static import copy_static
from page_creation import generate_pages_recursive

if __name__ == "__main__":
    copy_static()
    generate_pages_recursive("content", "template.html", "public")