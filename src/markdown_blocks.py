from enum import Enum
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

# converts a block of markdown text into a list of 1 line blocks
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        lines = block.split("\n")
        stripped_lines = [line.strip() for line in lines]
        block = "\n".join(stripped_lines).strip()
        if block == "":
            continue
        filtered_blocks.append(block)
    return filtered_blocks

# create an Enum for the block types
class BlockType(Enum):

    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDEREDLIST = "unordered_list"
    ORDEREDLIST = "ordered_list"

# used to determine what the blocktype of each block should be
def block_to_block_type(markdown_block):
    words = markdown_block.split()
    first_word = words[0]
    if first_word.startswith("#") and len(first_word) <= 6 and all(c == '#' for c in first_word):
        return BlockType.HEADING
    elif first_word[:-1].isdigit() and first_word.endswith("."):
        return BlockType.ORDEREDLIST
    elif first_word == "-":
        return BlockType.UNORDEREDLIST
    elif first_word == ">":
        return BlockType.QUOTE
    elif markdown_block.startswith("```") and markdown_block.endswith("```"):
        return BlockType.CODE
    return BlockType.PARAGRAPH

#creates child nodes for the 
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            tag_count = block.split()[0].count("#")
            node = ParentNode(f"h{tag_count}", text_to_children(block[tag_count+1:]))
            children.append(node)
        elif block_type == BlockType.PARAGRAPH:
            lines = block.split("\n")
            cleaned_lines = [line.strip(" ") for line in lines]
            join_block = " ".join(cleaned_lines)
            node = ParentNode("p", text_to_children(join_block))
            children.append(node)
        elif block_type == BlockType.CODE:
            clean_block = block[3:-3].lstrip("\n")
            text_node = TextNode(clean_block, TextType.CODE)
            code_node = text_node_to_html_node(text_node)
            node = ParentNode("pre", [code_node])
            children.append(node)
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            cleaned_lines = [line.lstrip("> ") for line in lines]
            joined = " ".join(cleaned_lines)
            node = ParentNode("blockquote", text_to_children(joined))
            children.append(node)
        elif block_type == BlockType.UNORDEREDLIST:
            lines = block.split("\n")
            inline_parents = []
            for line in lines:
                clean_line = line[2:]
                inline_children = text_to_children(clean_line)
                inline_parent = ParentNode("li", inline_children)
                inline_parents.append(inline_parent)
            node = ParentNode("ul", inline_parents)
            children.append(node)
        elif block_type == BlockType.ORDEREDLIST:
            lines = block.split("\n")
            inline_parents = []
            for line in lines:
                clean_line = line.split(". ", 1)[1]
                inline_children = text_to_children(clean_line)
                inline_parent = ParentNode("li", inline_children)
                inline_parents.append(inline_parent)
            node = ParentNode("ol", inline_parents)
            children.append(node)

    return ParentNode("div", children)
