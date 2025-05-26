from textnode import TextNode, TextType
from extract import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if(node.text_type != TextType.TEXT):
            new_nodes.append(node)
            continue
        
        split_text = node.text.split(delimiter)

        if(len(split_text) % 2 == 0):
            raise Exception("detected unmatched delimiter")

        for i in range(0, len(split_text)):
            if split_text[i] == "":
                continue
            
            if i % 2 == 0:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT))      
            else:
                new_nodes.append(TextNode(split_text[i], text_type))      


    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        matches = extract_markdown_images(node.text)

        if len(matches) == 0:
            new_nodes.append(node)
            continue
        
        text = node.text
        for match in matches:
            split = text.split(f"![{match[0]}]({match[1]})", 1)

            if(split[0] != ""):
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            
            new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))

            text = split[1]
        
        if(text != ""):
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        matches = extract_markdown_links(node.text)

        if len(matches) == 0:
            new_nodes.append(node)
            continue
        
        text = node.text
        for match in matches:
            split = text.split(f"[{match[0]}]({match[1]})", 1)

            if(split[0] != ""):
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            
            new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))

            text = split[1]
        
        if(text != ""):
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes