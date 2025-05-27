import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()