from htmlnode import HTMLNode

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
            
