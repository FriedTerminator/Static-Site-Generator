import unittest

from textnode import TextNode, TextType, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnode, markdown_to_blocks


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
        self.assertListEqual(nodes, [TextNode("Text with ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT)])

    def test_split_delimiter_italic(self):
        node = TextNode("Text with _italic_ word", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(nodes, [TextNode("Text with ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT)])

    def test_split_delimiter_italic(self):
        node = TextNode("Text with `code` word", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(nodes, [TextNode("Text with ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" word", TextType.TEXT)])

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
            "This is a text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("This is a text with a link ", TextType.TEXT),
                             TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                             TextNode(" and ", TextType.TEXT),
                             TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")], new_nodes)
        
    def test_text_to_textnode_bold(self):
        text = "This text has a **bold** word"
        result = text_to_textnode(text)
        self.assertListEqual([TextNode("This text has a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT)], result)

    def test_text_to_textnode_italic(self):
        text = "This text has a _italic_ word"
        result = text_to_textnode(text)
        self.assertListEqual([TextNode("This text has a ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT)], result)

    def test_text_to_textnode_code(self):
        text = "This text has a `code` word"
        result = text_to_textnode(text)
        self.assertListEqual([TextNode("This text has a ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" word", TextType.TEXT)], result)

    def test_text_to_textnode_all_delimiters(self):
        text = "This text has a **bold** and _italic_ and `code` word"
        result = text_to_textnode(text)
        self.assertListEqual([TextNode("This text has a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" and ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" and ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" word", TextType.TEXT)], result)

    def test_text_to_textnode_image(self):
        text = "This is a text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)"
        result = text_to_textnode(text)
        self.assertListEqual([TextNode("This is a text with an image ", TextType.TEXT),
                             TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
                             TextNode(" and ", TextType.TEXT),
                             TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev")], result)
        
    def test_text_to_textnode_link(self):
        text = "This is a text with a link [to google](https://www.google.com) and [to steam](https://www.steam.com)"
        result = text_to_textnode(text)
        self.assertListEqual([TextNode("This is a text with a link ", TextType.TEXT),
                             TextNode("to google", TextType.LINK, "https://www.google.com"),
                             TextNode(" and ", TextType.TEXT),
                             TextNode("to steam", TextType.LINK, "https://www.steam.com")], result)
        
    def test_text_to_textnode_with_all(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnode(text)
        self.assertListEqual([TextNode("This is ", TextType.TEXT),
                            TextNode("text", TextType.BOLD),
                            TextNode(" with an ", TextType.TEXT),
                            TextNode("italic", TextType.ITALIC),
                            TextNode(" word and a ", TextType.TEXT),
                            TextNode("code block", TextType.CODE),
                            TextNode(" and an ", TextType.TEXT),
                            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                            TextNode(" and a ", TextType.TEXT),
                            TextNode("link", TextType.LINK, "https://boot.dev")], result)
        
    def test_markdown_to_blocks(self):
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_single(self):
        md = """
            This is a single line
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a single line",
            ],
        )

    def test_markdown_to_blocks_empty_line(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,[])
    
    def test_markdown_to_blocks_multiple_paragraphs(self):
        md = """
            First Paragraph

            Second Paragraph
            with two lines

            Third Paragraph
            with
            three lines
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First Paragraph",
                "Second Paragraph\nwith two lines",
                "Third Paragraph\nwith\nthree lines"
            ],
        )

if __name__ == "__main__":
    unittest.main()