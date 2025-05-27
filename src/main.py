from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    example_node = HTMLNode(
        tag="a",
        value="Google",
        props={
            "href": "https://www.google.com",
            "target": "_blank"
        }
    )

    print(example_node)
    print("HTML Attributes:", example_node.props_to_html())

if __name__ == "__main__":
    main()