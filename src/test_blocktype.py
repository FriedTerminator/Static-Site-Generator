import unittest
from blocktype import BlockType, block_to_block_type

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

if __name__ == "__main__":
    unittest.main()