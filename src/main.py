from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    node = TextNode("test text", TextType.LINK, "https://www.boot.dev")
    print(node)

main()


