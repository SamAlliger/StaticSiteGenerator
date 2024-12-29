import unittest

from markdown_to_html import markdown_to_html_node
from htmlnode import ParentNode, LeafNode

class TestMarkdownToHTML(unittest.TestCase):
    def test_MarkdownToHTML(self):
        markdown = "# This is a Header1\n\n## And a Header2\n\nAnd a Paragraph with some text"
        actual = markdown_to_html_node(markdown).__repr__()
        expected = ParentNode("div",
            [
            ParentNode("h1",
                [
                LeafNode(None, "This is a Header1")
                ]
            ),
            ParentNode("h2",
                [
                LeafNode(None, "And a Header2")
                ]
            ),
            ParentNode("p",
                [
                LeafNode(None, "And a Paragraph with some text")
                ]
            )
            ]
        ).__repr__()
        self.assertEqual(actual, expected)

    def test_MarkdownToHTML2(self):
        markdown = "# This is a Header1\n\n## And a Header2\n\n###### And a Header6\n\nAnd a Paragraph with some **bold** text and a [link](https://www.boot.dev) and an ![image](https://i.imgur.com/aKaOqIh.gif)\n\n```And some code```\n\n* This is the first list item in an unorded list\n* This is a list item\n- This is another list item\n\n1. This is the first list item in an ordered list\n2. This is a list item with some *italic* text"
        actual = markdown_to_html_node(markdown).__repr__()
        expected = ParentNode("div",
            [
            ParentNode("h1",
                [
                LeafNode(None, "This is a Header1")
                ]
            ),
            ParentNode("h2",
                [
                LeafNode(None, "And a Header2")
                ]
            ),
            ParentNode("h6",
                [
                LeafNode(None, "And a Header6")
                ]
            ),
            ParentNode("p",
                [
                LeafNode(None, "And a Paragraph with some "),
                LeafNode("b", "bold"),
                LeafNode(None, " text and a "),
                LeafNode("a", "link", {"href":"https://www.boot.dev"}),
                LeafNode(None, " and an "),
                LeafNode("img", "", {"src":"https://i.imgur.com/aKaOqIh.gif", "alt":"image"})
                ]
            ),
            ParentNode("pre",
                [
                ParentNode("code",
                    [
                    LeafNode(None, "And some code")
                    ]
                ),
                ]
            ),
            ParentNode("ul",
                [
                ParentNode("li",
                    [
                    LeafNode(None, "This is the first list item in an unorded list")
                    ]
                ),
                ParentNode("li",
                    [
                    LeafNode(None, "This is a list item")
                    ]
                ),
                ParentNode("li",
                    [
                    LeafNode(None, "This is another list item")
                    ]
                )
                ]
            ),
            ParentNode("ol",
                [
                ParentNode("li",
                    [
                    LeafNode(None, "This is the first list item in an ordered list")
                    ]
                ),
                ParentNode("li",
                    [
                    LeafNode(None, "This is a list item with some "),
                    LeafNode("i", "italic"),
                    LeafNode(None, " text")
                    ]
                )
                ]
            )
            ]
        ).__repr__()
        self.assertEqual(actual, expected)