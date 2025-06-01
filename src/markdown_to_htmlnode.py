from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from htmlnode import HTMLNode
from text_to_nodes import text_to_textnodes
from textnode_to_htmlnode import text_node_to_html_node
from textnode import TextNode, TextType
from parentnode import ParentNode
import re

def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)

    children = list()

    for block in blocks:
        block_parent_node = block_to_htmlnode(block)
        children.append(block_parent_node)
    
    return ParentNode("div", children, None)


def text_to_children(text):
    textnode_children = text_to_textnodes(text)

    children = list()

    for textnode in textnode_children:
        children.append(text_node_to_html_node(textnode))

    return children


def block_to_htmlnode(block):
    type = block_to_block_type(block)
    
    match type:
        case BlockType.PARAGRAPH:
            return p_to_node(block)
        case BlockType.HEADING:
            return h_to_node(block)
        case BlockType.CODE:
            return c_to_node(block)
        case BlockType.QUOTE:
            return q_to_node(block)
        case BlockType.ULIST:
            return ul_to_node(block)
        case BlockType.OLIST:
            return ol_to_node(block)
        case _:
            raise Exception(f"{type} is invalid blocktype")


def p_to_node(block):
    split = block.split("\n")
    text = " ".join(split)

    children = text_to_children(text)
    
    return ParentNode("p", children)


def h_to_node(block):
    num = len(re.findall(r"#", block[0:7]))
    
    if(num < 1 or num > 6):
        raise Exception("invalid header syntax")
    
    text = block[num + 1:]

    children = text_to_children(text)
    
    return ParentNode(f"h{num}", children)


def c_to_node(block):
    text = block.strip("```").lstrip("\n")

    child = text_node_to_html_node(TextNode(text, TextType.TEXT))
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def q_to_node(block):
    lines = block.split("\n")
    new_lines = []

    for line in lines:
        new_line = line.lstrip(">").strip()
        new_lines.append(new_line)

    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)


def ul_to_node(block):
    lines = block.split("\n")
    upper_children = []

    for line in lines:
        text = line.lstrip("-").strip()
        lower_children = text_to_children(text)
        upper_children.append(ParentNode("li", lower_children))

    return ParentNode("ul", upper_children)


def ol_to_node(block):
    lines = block.split("\n")
    upper_children = []

    for line in lines:
        text = line[2:].strip()
        lower_children = text_to_children(text)
        upper_children.append(ParentNode("li", lower_children))

    return ParentNode("ol", upper_children)