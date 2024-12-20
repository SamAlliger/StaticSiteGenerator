from textnode import TextNode
from textnode import TextType

def main():
    Test = TextNode("This is a text node", TextType.bold.value, "https://test.com")
    Test.__repr__()

main()