from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    example_node = LeafNode(
        tag="a",
        value="Google",
        props={
            "href": "https://www.google.com",
            "target": "_blank"
        }
    )

    print(example_node)
    print("Leaf Attributes:", example_node.to_html())

if __name__ == "__main__":
    main()