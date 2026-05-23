import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            parts = old_node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception("that's invalid Markdown syntax")
            for i, value in enumerate(parts):
                if i % 2 == 0:
                    node = TextNode(value, TextType.TEXT)
                else:
                    node = TextNode(value, text_type)
                new_nodes.append(node)
    return new_nodes 

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            results = extract_markdown_images(node.text)
            if not results:
                new_nodes.append(node)
                continue
            original_text = node.text
            for result in results:
                sections = original_text.split(f"![{result[0]}]({result[1]})", 1)
                if sections[0] != "":
                    new_text_node = TextNode(sections[0], TextType.TEXT, None)
                    new_nodes.append(new_text_node)
                new_image_node = TextNode(result[0], TextType.IMAGE, result[1])
                new_nodes.append(new_image_node)
                original_text = sections[1]
            if original_text:
                new_text_node2 = TextNode(original_text, TextType.TEXT, None)
                new_nodes.append(new_text_node2)
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            results = extract_markdown_links(node.text)
            if not results:
                new_nodes.append(node)
                continue
            original_text = node.text
            for result in results:
                sections = original_text.split(f"[{result[0]}]({result[1]})", 1)
                if sections[0] != "":
                    new_text_node = TextNode(sections[0], TextType.TEXT, None)
                    new_nodes.append(new_text_node)
                new_link_node = TextNode(result[0], TextType.LINK, result[1])
                new_nodes.append(new_link_node)
                original_text = sections[1]
            if original_text:
                new_text_node2 = TextNode(original_text, TextType.TEXT, None)
                new_nodes.append(new_text_node2)
        else:
            new_nodes.append(node)
    return new_nodes