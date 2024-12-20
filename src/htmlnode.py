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
        print(f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All Leaf Nodes must have a value.")
        if self.tag == None:
            return self.value
        return "<" + self.tag + self.props_to_html() + ">" + self.value + "</" + self.tag + ">"
    
    def __repr__(self):
        print(f"LeafNode({self.tag}, {self.value}, {self.props})")