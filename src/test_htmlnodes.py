import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()