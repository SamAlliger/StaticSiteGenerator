import unittest

from textnode import TextNode, TextType
from textnode_conversion import split_nodes_delimiter, split_nodes_image, split_nodes_link

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

class TestTextNodeImageExtraction(unittest.TestCase):
    def test_image1(self):
        node = TextNode("This is text with an image of ![boots](https://www.boot.dev) and ![a thumbnail](https://www.youtube.com/@bootdotdev)", TextType.normal)
        actual = split_nodes_image([node])
        expected = [
            TextNode("This is text with an image of ", TextType.normal),
            TextNode("boots", TextType.image, "https://www.boot.dev"),
            TextNode(" and ", TextType.normal),
            TextNode("a thumbnail", TextType.image, "https://www.youtube.com/@bootdotdev")
            ]
        self.assertEqual(actual, expected)
    def test_image2(self):
        node = TextNode("This is text with an image of ![boots](https://www.boot.dev) and ![a thumbnail](https://www.youtube.com/@bootdotdev) and something at the end", TextType.normal)
        actual = split_nodes_image([node])
        expected = [
            TextNode("This is text with an image of ", TextType.normal),
            TextNode("boots", TextType.image, "https://www.boot.dev"),
            TextNode(" and ", TextType.normal),
            TextNode("a thumbnail", TextType.image, "https://www.youtube.com/@bootdotdev"),
            TextNode(" and something at the end", TextType.normal)
            ]
        self.assertEqual(actual, expected)
    def test_image3(self):
        node = TextNode("This is text with no image", TextType.normal)
        actual = split_nodes_image([node])
        expected = [TextNode("This is text with no image", TextType.normal)]
        self.assertEqual(actual, expected)
    def test_image4(self):
        node = [
            TextNode("This is text with an image of ![boots](https://www.boot.dev) and ![a thumbnail](https://www.youtube.com/@bootdotdev)", TextType.normal),
            TextNode("and another with a ![random puppy](https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da)", TextType.normal)
        ]
        actual = split_nodes_image(node)
        expected = [
            TextNode("This is text with an image of ", TextType.normal),
            TextNode("boots", TextType.image, "https://www.boot.dev"),
            TextNode(" and ", TextType.normal),
            TextNode("a thumbnail", TextType.image, "https://www.youtube.com/@bootdotdev"),
            TextNode("and another with a ", TextType.normal),
            TextNode("random puppy", TextType.image, "https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da")
        ]
        self.assertEqual(actual, expected)

class TestTextNodeLinkExtraction(unittest.TestCase):
    def test_link1(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.normal)
        actual = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.normal),
            TextNode("to boot dev", TextType.link, "https://www.boot.dev"),
            TextNode(" and ", TextType.normal),
            TextNode("to youtube", TextType.link, "https://www.youtube.com/@bootdotdev")
            ]
        self.assertEqual(actual, expected)
    def test_link2(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and something at the end", TextType.normal)
        actual = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.normal),
            TextNode("to boot dev", TextType.link, "https://www.boot.dev"),
            TextNode(" and ", TextType.normal),
            TextNode("to youtube", TextType.link, "https://www.youtube.com/@bootdotdev"),
            TextNode(" and something at the end", TextType.normal)
            ]
        self.assertEqual(actual, expected)
    def test_link3(self):
        node = TextNode("This is text with no link", TextType.normal)
        actual = split_nodes_link([node])
        expected = [TextNode("This is text with no link", TextType.normal)]
        self.assertEqual(actual, expected)
    def test_link4(self):
        node = [
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.normal),
            TextNode("and another with a [random puppy](https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da)", TextType.normal)
        ]
        actual = split_nodes_link(node)
        expected = [
            TextNode("This is text with a link ", TextType.normal),
            TextNode("to boot dev", TextType.link, "https://www.boot.dev"),
            TextNode(" and ", TextType.normal),
            TextNode("to youtube", TextType.link, "https://www.youtube.com/@bootdotdev"),
            TextNode("and another with a ", TextType.normal),
            TextNode("random puppy", TextType.link, "https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da")
        ]
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()