from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    normal = "normal"
    bold = "bold"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(TextNode, TextNode2):
        if TextNode.text == TextNode2.text and TextNode.text_type == TextNode2.text_type and TextNode.url == TextNode2.url:
            return True
        return False

    def __repr__(TextNode):
        return f"TextNode({TextNode.text}, {TextNode.text_type}, {TextNode.url})"
    
    def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.normal:
            return LeafNode(None, text_node.text)
        if text_node.text_type == TextType.bold:
            return LeafNode("b", text_node.text)
        if text_node.text_type == TextType.italic:
            return LeafNode("i", text_node.text)
        if text_node.text_type == TextType.code:
            return LeafNode("code", text_node.text)
        if text_node.text_type == TextType.link:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        if text_node.text_type == TextType.image:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        raise Exception(f"{text_node.text_type} is not a valid TextType")

    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes=[]
        for node in old_nodes:
            if node.text_type != TextType.Normal:
                new_nodes.append(node)
            if len(node.split(delimiter)) % 2 != 0:
                raise Exception("Invalid Markdown syntax")
            else:
                split_nodes = node.split(delimiter)
                for i in range(0, len(split_nodes)):
                    if i % 2 != 0:
                        new_nodes.append(TextNode(split_nodes[i], TextType.normal))
                    else:
                        new_nodes.append(TextNode(split_nodes[i], text_type))
        return new_nodes