from split_nodes import split_nodes_link, split_nodes_delimiter, split_nodes_image
from textnode import TextNode, TextType

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    
    return split_nodes_image(split_nodes_link(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter([node], "**", TextType.BOLD), "_", TextType.ITALIC), "`", TextType.CODE)))