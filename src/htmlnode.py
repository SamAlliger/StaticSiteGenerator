class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        html = ""
        if self.props != None:
            for prop in self.props:
                html = html + " " + prop + "=\"" + self.props[prop] + "\""
        return html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All Leaf Nodes must have a value.")
        if self.tag == None:
            return self.value
        return "<" + self.tag + self.props_to_html() + ">" + self.value + "</" + self.tag + ">"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        html = []
        if self.tag == None:
            raise ValueError("All Parent Nodes must have a tag.")
        if self.children == None:
            raise ValueError("All Parent Nodes must have at least 1 children.")
        html.append("<" + self.tag + ">")
        for node in self.children:
            html.append(node.to_html())
        html.append("</" + self.tag + ">")
        return "".join(html)

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"