from htmlnode import HTMLNode
from textnode import TextType

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if(self.value == None):
            raise ValueError("LeafNode requires value")
        if(self.tag == None):
            return self.value
        
        match self.tag:
            case ("p"):
                return f"<p>{self.value}</p>"
            case ("a"):
                return f"<a{self.props_to_html()}>{self.value}</a>"
            case ("h1"):
                return f"<h1>{self.value}</h1>"
            case ("h2"):
                return f"<h2>{self.value}</h2>"
            case ("h3"):
                return f"<h3>{self.value}</h3>"
            case ("h4"):
                return f"<h4>{self.value}</h4>"
            case ("h5"):
                return f"<h5>{self.value}</h5>"
            case ("h6"):
                return f"<h6>{self.value}</h6>"
            case ("b"):
                return f"<b>{self.value}</b>"
            case ("i"):
                return f"<i>{self.value}</i>"
            case ("code"):
                return f"<code>{self.value}</code>"
            case ("span"):
                return f"<span>{self.value}</span>"
            case ("div"):
                return f"<div>{self.value}</div>"
            case ("img"):
                return f"<img{self.props_to_html()} />"
            case _:
                raise Exception(f"{self.tag} is invalid tag")
            
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case (TextType.TEXT):
            return LeafNode(None, text_node.text)
        case (TextType.BOLD):
            return LeafNode("b", text_node.text)
        case (TextType.ITALIC):
            return LeafNode("i", text_node.text)
        case (TextType.CODE):
            return LeafNode("code", text_node.text)
        case (TextType.LINK):
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case (TextType.IMAGE):
            return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Invalid text node type")