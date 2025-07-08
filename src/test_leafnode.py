import unittest
from leafnode import LeafNode
from htmlnode import HTMLNode
from textnode import TextType, TextNode
from leafnode import text_node_to_html_node

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello world")
        self.assertEqual(node.to_html(), "<p>Hello world</p>")

    def test_raw_text_node(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html_single_prop(self):
        node = LeafNode("a", "What's up", {"href":"https://goodvibes.com"})
        self.assertEqual(node.to_html(), '<a href="https://goodvibes.com">What\'s up</a>')
    
    def test_leaf_to_html_multiple_props(self):
        node = LeafNode("h1", "How is it going", {"href":"https://goodvibes.com", "target":"_blank"})
        self.assertEqual(node.to_html(), "<h1 href=\"https://goodvibes.com\" target=\"_blank\">How is it going</h1>")

    def test_leaf_tag_is_none(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_left_value_is_empty(self):
        node = LeafNode("span", "")
        self.assertEqual(node.to_html(), "<span></span>")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")
    
    def test_link(self):
        node = TextNode("This is a link text node", TextType.LINK, "example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props, {"href": "example.com"})

    def test_img(self):
        node = TextNode("alt text", TextType.IMAGE, "example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "example.com", "alt": "alt text"})

if __name__ == "__main__":
    unittest.main()