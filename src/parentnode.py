from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("A tag is required for a parent node")
        if not isinstance(children, list):
            children = [children]
        super().__init__(tag=tag,value =None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("A tag is required for a parent node")
        
        if not self.children:
            raise ValueError("Children are required for a parent node")
        
        children_html = "".join(child.to_html() for child in self.children)
        
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"