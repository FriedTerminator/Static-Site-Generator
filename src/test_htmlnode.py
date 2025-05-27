import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "", "Empty props should return empty string")

    def test_props_to_html_single(self):
        node = HTMLNode(props = {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"', "Single prop should format correctly")

    def test_props_to_html_multiple(self):
        node = HTMLNode(props = {" href": "https://www.google.com", " target": "_blank"})
        result = node.props_to_html()
        self.assertIn('href="https://www.google.com"', result)
        self.assertIn('target="_blank"', result)
        self.assertTrue(result.startswith(" "), "Should start with a space")

if __name__ == "__main__":
    unittest.main()