from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):

    TEXT = "plain text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        leafnode = LeafNode(None, text_node.text, None)
    elif text_node.text_type == TextType.BOLD:
        leafnode = LeafNode("b", text_node.text, None)
    elif text_node.text_type == TextType.ITALIC:
        leafnode = LeafNode("i", text_node.text, None)
    elif text_node.text_type == TextType.CODE:
        leafnode = LeafNode("code", text_node.text, None)
    elif text_node.text_type == TextType.LINK:
        leafnode = LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        leafnode = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("text node must have a text type")
    return leafnode