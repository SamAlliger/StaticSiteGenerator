import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()