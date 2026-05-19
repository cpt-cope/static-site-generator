import unittest
from htmlnode import HTMLNode, LeafNode

test_prop = {"href": "https://www.google.com", "target": "_blank"}
test_prop2 = {"href": "https://www.google.com"}


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "two props", None, test_prop)
        node2 = HTMLNode("a", "empty prop", None, {})
        node3 = HTMLNode("a", "one prop", None, test_prop2)
        result = node.props_to_html()
        result2 = node2.props_to_html()
        result3 = node3.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')
        self.assertEqual(result2, "")
        self.assertEqual(result3, ' href="https://www.google.com"')

    def test_repr(self):
        node = HTMLNode("a", "two props", None, test_prop)
        self.assertEqual(node.__repr__(), "HTMLNode(a, two props, None, {'href': 'https://www.google.com', 'target': '_blank'})")

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node1.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_repr(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node1.__repr__(), "LeafNode(p, This is a paragraph of text., None)")

if __name__ == "__main__":
    unittest.main()