import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestInlinMarkdown(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("some text with `code` in it", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("some text with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" in it", TextType.TEXT)
        ])

    def test_bold_delimiter(self):
        node = TextNode("some text with **bold text** in it", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("some text with ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" in it", TextType.TEXT)
        ])

    def test_italic_delimiter(self):
        node = TextNode("some text with _italic text_ in it", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(result, [
            TextNode("some text with ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" in it", TextType.TEXT)
        ])

    def test_multi_delimiter(self):
        node = TextNode("some text with `code block 1` and `code block 2` in it", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("some text with ", TextType.TEXT),
            TextNode("code block 1", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("code block 2", TextType.CODE),
            TextNode(" in it", TextType.TEXT)
        ])

    def test_unclosed_delimiter(self):
        node = TextNode("some text with `code unclosed in it", TextType.TEXT)
        with self.assertRaisesRegex(Exception, "that's invalid Markdown syntax"):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_non_text_node(self):
        node = TextNode("`code block`", TextType.CODE)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [TextNode("`code block`", TextType.CODE)])



if __name__ == "__main__":
    unittest.main()