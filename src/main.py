from textnode import TextNode, TextType

def main():
    node = TextNode("Hello, world!", TextType.TEXT)
    print(node)

if __name__ == "__main__":
    main()