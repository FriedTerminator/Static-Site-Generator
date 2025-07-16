import unittest
from blocktype import BlockType, block_to_block_type, markdown_to_html_node
from htmlnode import HTMLNode

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        block = "### Heading"
        result = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, result)

    def test_code(self):
        block = "``` This is a code block ```"
        result = block_to_block_type(block)
        self.assertEqual(BlockType.CODE, result)

    def test_quote(self):
        block = ">first quote\n>second quote"
        result = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, result)

    def test_unordered_list(self):
        block = "- Fruit\n- Vegetables\n- Meats"
        result = block_to_block_type(block)
        self.assertEqual(BlockType.UNORDERED_LIST, result)

    def test_ordered_list(self):
        block = "1. Mississippi\n2. Alabama\n3. New York"
        result = block_to_block_type(block)
        self.assertEqual(BlockType.ORDERED_LIST, result)

    def test_regular_paragraph(self):
        block = "This is a\nregular\nparagraph"
        result = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, result)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_output_of_unordered_list(self):
        md = """
- This is a list
- of stuff
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>of stuff</li></ul></div>",
        )

    def test_output_of_ordered_list(self):
        md = """
1. This is a list
2. of stuff
3. such as groceries
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is a list</li><li>of stuff</li><li>such as groceries</li></ol></div>",
        )

    def test_html_of_quote(self):
        md = """
>You either die a hero or live long enough to see yourself become the villain
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>You either die a hero or live long enough to see yourself become the villain</blockquote></div>",
        )

if __name__ == "__main__":
    unittest.main()