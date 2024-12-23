import unittest

from textnode import TextNode, TextType
from textnode_conversion import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.bold, "https://url.com")
        node2 = TextNode("This is a text node", TextType.bold, "https://url.com")
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.italic, "https://url.com")
        node2 = TextNode("This is a text node", TextType.bold, "https://url.com")
        self.assertNotEqual(node, node2)

    def test_noteq2(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold, "https://url.com")
        self.assertNotEqual(node, node2)

    def test_noteq3(self):
        node = TextNode("This is a text node", TextType.bold, "https://url.com")
        node2 = TextNode("This is a different text node", TextType.bold, "https://url.com")
        self.assertNotEqual(node, node2)

class TestTextNodeConversion(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a normal text node", TextType.normal).text_node_to_html_node()
        actual = node.__repr__()
        expected = "LeafNode(None, This is a normal text node, None)"
        self.assertEqual(actual, expected)
    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.bold).text_node_to_html_node()
        actual = node.__repr__()
        expected = "LeafNode(b, This is a bold text node, None)"
        self.assertEqual(actual, expected)
    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.italic).text_node_to_html_node()
        actual = node.__repr__()
        expected = "LeafNode(i, This is an italic text node, None)"
        self.assertEqual(actual, expected)
    def test_code(self):
        node = TextNode("This is a code text node", TextType.code).text_node_to_html_node()
        actual = node.__repr__()
        expected = "LeafNode(code, This is a code text node, None)"
        self.assertEqual(actual, expected)
    def test_link(self):
        node = TextNode("This is a link text node", TextType.link, "https://url.com").text_node_to_html_node()
        actual = node.__repr__()
        expected = "LeafNode(a, This is a link text node, {'href': 'https://url.com'})"
        self.assertEqual(actual, expected)
    def test_image(self):
        node = TextNode("This is a image text node", TextType.image, "https://url.com").text_node_to_html_node()
        actual = node.__repr__()
        expected = "LeafNode(img, , {'src': 'https://url.com', 'alt': 'This is a image text node'})"
        self.assertEqual(actual, expected)

class TestTextNodeSplit(unittest.TestCase):
    def test_1split(self):
        node = TextNode("This is text with a `code block` word", TextType.normal)
        actual = split_nodes_delimiter([node], "`", TextType.code)
        expected = [
            TextNode("This is text with a ", TextType.normal),
            TextNode("code block", TextType.code),
            TextNode(" word", TextType.normal),
        ]
        self.assertEqual(actual, expected)
    def test_2split(self):
        node = [
            TextNode("This is text with a `code block` word", TextType.normal),
            TextNode("and another with a `code block` word", TextType.normal)
        ]
        actual = split_nodes_delimiter(node, "`", TextType.code)
        expected = [
            TextNode("This is text with a ", TextType.normal),
            TextNode("code block", TextType.code),
            TextNode(" word", TextType.normal),
            TextNode("and another with a ", TextType.normal),
            TextNode("code block", TextType.code),
            TextNode(" word", TextType.normal),
        ]
        self.assertEqual(actual, expected)
    def test_nosplit(self):
        node = [
            TextNode("This is text with a `code block` word", TextType.normal),
            TextNode("and another with a `code block` word", TextType.normal),
            TextNode("and a bold one that shouldn't be split", TextType.bold)
        ]
        actual = split_nodes_delimiter(node, "`", TextType.code)
        expected = [
            TextNode("This is text with a ", TextType.normal),
            TextNode("code block", TextType.code),
            TextNode(" word", TextType.normal),
            TextNode("and another with a ", TextType.normal),
            TextNode("code block", TextType.code),
            TextNode(" word", TextType.normal),
            TextNode("and a bold one that shouldn't be split", TextType.bold),
        ]
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()