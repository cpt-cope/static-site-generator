from textnode import TextNode, TextType


def main():
    node = TextNode("test text", TextType.LINKS, "https://www.boot.dev")
    print(node)

main()


