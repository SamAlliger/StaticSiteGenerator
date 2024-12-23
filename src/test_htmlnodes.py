import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_prop(self):
        node = HTMLNode("p", "text", None, {})
        actual = node.props_to_html()
        expected = ""
        self.assertEqual(actual, expected)
    def test_prop2(self):
        node = HTMLNode("p", "text", None, {"href": "https://url.com"})
        actual = node.props_to_html()
        expected = " href=\"https://url.com\""
        self.assertEqual(actual, expected)
    def test_prop3(self):
        node = HTMLNode("p", "text", None, {"href": "https://url.com", "target": "_blank"})
        actual = node.props_to_html()
        expected = " href=\"https://url.com\" target=\"_blank\""
        self.assertEqual(actual, expected)
    
class TestLeafNodes(unittest.TestCase):
    def test_leaf(self):
        node = LeafNode(None, "This is a test node")
        actual = node.to_html()
        expected = "This is a test node"
        self.assertEqual(actual, expected)
    def test_leaf2(self):
        node = LeafNode("a", "This is a test link", props={"href": "https://url.com"})
        actual = node.to_html()
        expected = "<a href=\"https://url.com\">This is a test link</a>"
        self.assertEqual(actual, expected)
    def test_leaf3(self):
        node = LeafNode("h1", "This is a heading")
        actual = node.to_html()
        expected = "<h1>This is a heading</h1>"
        self.assertEqual(actual, expected)

class TestParentNodes(unittest.TestCase):
    def test_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        actual = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(actual, expected)
    def test_parent2(self):
        node = ParentNode(
            "h1",
            [
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("a", "This is a test link", props={"href": "https://url.com"}),
                        LeafNode(None, "This is a test node")
                    ]
                ),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        actual = node.to_html()
        expected = "<h1>Normal text<p><a href=\"https://url.com\">This is a test link</a>This is a test node</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</h1>"
        self.assertEqual(actual, expected)
    def test_parent3(self):
        node = ParentNode(
            "h1",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("a", "This is a test link", props={"href": "https://url.com"}),
                        LeafNode(None, "This is a test node")
                    ]
                ),
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "This is a test node"),
                        LeafNode("a", "This is a test link", props={"href": "https://url.com"})
                    ]
                )
            ]
        )
        actual = node.to_html()
        expected = "<h1><p><a href=\"https://url.com\">This is a test link</a>This is a test node</p><p>This is a test node<a href=\"https://url.com\">This is a test link</a></p></h1>"
        self.assertEqual(actual, expected)
    def test_parent4(self):
        node = ParentNode("p", [])
        actual = node.to_html()
        expected = "<p></p>"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()