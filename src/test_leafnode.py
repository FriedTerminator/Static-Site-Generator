import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello world")
        self.assertEqual(node.to_html(), "<p>Hello world</p>")

    def test_leaf_to_html_single_prop(self):
        node = LeafNode("a", "What's up", {"href":"https://goodvibes.com"})
        self.assertEqual(node.to_html(), '<a href="https://goodvibes.com">What\'s up</a>')
    
    def test_leaf_to_html_multiple_props(self):
        node = LeafNode("h1", "How is it going", {"href":"https://goodvibes.com", "target":"_blank"})
        self.assertEqual(node.to_html(), "<h1 href=\"https://goodvibes.com\" target=\"_blank\">How is it going</h1>")

if __name__ == "__main__":
    unittest.main()