from htmlnode import HTMLNode
from textnode import TextType

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode requires a non-None value")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All LeafNodes must have a value")
        
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
def text_node_to_html_node(text_node):
    if(text_node.text_type == TextType.TEXT):
        return LeafNode(None, text_node.text)
    if(text_node.text_type == TextType.BOLD):
        return LeafNode("b", text_node.text)     
    if(text_node.text_type == TextType.ITALIC):
        return LeafNode("i", text_node.text)     
    if(text_node.text_type == TextType.CODE):
        return LeafNode("code", text_node.text)     
    if(text_node.text_type == TextType.LINK):
        return LeafNode("a", text_node.text, {"href": text_node.url})     
    if(text_node.text_type == TextType.IMAGE):
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       