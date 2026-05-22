import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )
        

def test_parent_with_multiple_children(self):
    node = ParentNode("p", [
        LeafNode("b", "Bold"),
        LeafNode(None, " plain "),
        LeafNode("i", "Italic"),
    ])
    self.assertEqual(
        node.to_html(),
        "<p><b>Bold</b> plain <i>Italic</i></p>"
    )   

def test_nested_parent_nodes(self):
    inner = ParentNode("span", [
        LeafNode(None, "hello")
    ])
    outer = ParentNode("div", [inner])
    self.assertEqual(
        outer.to_html(),
        "<div><span>hello</span></div>"
    )

def test_parent_missing_tag_raises(self):
    node = ParentNode(None, [LeafNode(None, "text")])
    with self.assertRaises(ValueError):
        node.to_html()

def test_parent_with_empty_children(self):
    node = ParentNode("div", [])
    self.assertEqual(node.to_html(), "<div></div>")

if __name__ == "__main__":
    unittest.main()