import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("li", "child")
        parent_node = ParentNode("p", [child_node])
        self.assertEqual(parent_node.to_html(), "<p><li>child</li></p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = LeafNode("li", "child")
        parent_node = ParentNode("p", [child_node, grandchild_node])
        self.assertEqual(parent_node.to_html(), "<p><li>child</li><b>grandchild</b></p>")

    def test_to_html_with_parentnode_child(self):
        child_node = LeafNode("p", "This is great")
        parent_node2 = ParentNode("h2", [child_node])
        parent_node = ParentNode("h1", [parent_node2])
        self.assertEquals(parent_node.to_html(), "<h1><h2><p>This is great</p></h2></h1>")

    def test_to_html_mixed(self):
        child_node = LeafNode("p", "This is great")
        parent_node2 = ParentNode("h2", [child_node])
        parent_node = ParentNode("h1", [child_node, parent_node2])
        self.assertEquals(parent_node.to_html(), "<h1><p>This is great</p><h2><p>This is great</p></h2></h1>")

    def test_no_tag(self):
        child = LeafNode("p", "content")
        with self.assertRaises(ValueError):
            ParentNode(None, [child], {"href":"https://google.com"})

if __name__ == "__main__":
    unittest.main()