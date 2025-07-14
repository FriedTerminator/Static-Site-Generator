import unittest

from textnode import TextNode, TextType, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_test(self):
        node = TextNode("Text A", TextType.BOLD)
        node2 = TextNode("Text B", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_equal_none_url(self):
        node = TextNode("This is a text node", TextType.CODE, None)
        node2 = TextNode("This is a text node", TextType.CODE, None)
        self.assertEqual(node, node2)

    def test_not_equal_type(self):
        node = TextNode("Hello world", TextType.BOLD, "https://hello.com")
        node2 = TextNode("Hello world", TextType.ITALIC, "https://hello.com")
        self.assertNotEqual(node, node2)

    def test_equal_url(self):
        node = TextNode("What's up", TextType.TEXT, "https://coolmathgames.com")
        node2 = TextNode("What's up", TextType.TEXT, "https://coolmathgames.com")
        self.assertEqual(node, node2)

    def test_not_equal_url(self):
        node = TextNode("Image", TextType.IMAGE, "https://image.com")
        node2 = TextNode("Image", TextType.IMAGE, "https://coolimage.com")
        self.assertNotEqual(node, node2)

    def test_split_delimiter_bold(self):
        node = TextNode("Text with **bold** word", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(nodes, [TextNode("Text with", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode("word", TextType.TEXT)])

    def test_split_delimiter_italic(self):
        node = TextNode("Text with _italic word", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(nodes, [TextNode("Text with", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode("word", TextType.TEXT)])

    def test_split_delimiter_italic(self):
        node = TextNode("Text with `code` word", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(nodes, [TextNode("Text with", TextType.TEXT), TextNode("code", TextType.CODE), TextNode("word", TextType.TEXT)])

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_node_image(self):
        node = TextNode(
            "This is a text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("This is a text with an image ", TextType.TEXT),
                             TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
                             TextNode(" and ", TextType.TEXT),
                             TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev")], new_nodes)
        
    def test_split_node_link(self):
        node = TextNode(
            "This is a text with an image [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("This is a text with an image ", TextType.TEXT),
                             TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                             TextNode(" and ", TextType.TEXT),
                             TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")], new_nodes)

if __name__ == "__main__":
    unittest.main()