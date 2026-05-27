import unittest
from markdown_blocks import markdown_to_blocks, BlockType, block_to_block_type

class TestMarkdownBlocks(unittest.TestCase):

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

    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)

    def test_single_line_code(self):
        self.assertEqual(block_to_block_type("```# code comment```"), BlockType.CODE)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. Item"), BlockType.ORDEREDLIST)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- Item"), BlockType.UNORDEREDLIST)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> Quote"), BlockType.QUOTE)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("Just text."), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()