from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required")
        if self.children is None:
            raise ValueError("Parent must have children")
        child_body = ""
        for child in self.children:
            child_body += child.to_html()
        if self.props is None:
            return f"<{self.tag}>{child_body}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{child_body}</{self.tag}>"

