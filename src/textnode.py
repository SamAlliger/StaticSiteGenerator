from enum import Enum

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
        self.text_type= text_type
        self.url = url

    def __eq__(TextNode, TextNode2):
        if TextNode.text == TextNode2.text and TextNode.text_type == TextNode2.text_type and TextNode.url == TextNode2.url:
            return True
        return False

    def __repr__(TextNode):
        print(f"TextNode({TextNode.text}, {TextNode.text_type}, {TextNode.url})")