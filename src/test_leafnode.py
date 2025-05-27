import unittest
from leafnode import LeafNode

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

    

if __name__ == "__main__":
    unittest.main()