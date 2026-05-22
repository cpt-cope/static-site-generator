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

            
