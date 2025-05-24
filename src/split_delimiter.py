from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = list()
    
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
