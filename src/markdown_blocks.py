from enum import Enum
from htmlnode import HTMLNode

# converts a block of markdown text into 1 line blocks
def markdown_to_blocks(markdown):
    return [block.strip() for block in markdown.split("\n\n") if block.strip()]

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

# uses the block to block type tool to get find out the block type of a block
def get_block_type(blocks):
    for block in blocks:
        block_type = block_to_block_type(block)
    return block, block_type

# determines which header count the given header is
def header(block):
    return (block[0].stringcount("#"))

# creats an html node with the right tag for the block type
# incomplete
def block_to_html_node(block_type, block):
    if block_type == BlockType.HEADING:
        return HTMLNode(f"<h{header(block)}>")
    elif block_type == BlockType.QUOTE:
        return HTMLNode("<blockquote>")

# incomplete
def markdown_to_html_node(markdown):
    pass

