class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        props_string = ""
        for k, v in self.props.items():
            props_string += f'{k}="{v}"'
        return props_string.lstrip()

    def __repr__(self):
        return f"tag: {self.tag};\nvalue: {self.value};\nchildren: {self.children};\nprops: {self.props};"



