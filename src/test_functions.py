import unittest

from markdown_extraction import extract_markdown_images, extract_markdown_links, markdown_to_blocks, block_to_block_type

class TestMarkDownExtraction(unittest.TestCase):
    def test_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        actual = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(actual, expected)
    def test_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        actual = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(actual, expected)

class TestMarkDownSplitting(unittest.TestCase):
    def test_document_to_blocks(self):
        markdown = """# This is a heading

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            * This is the first list item in a list block
            * This is a list item
            * This is another list item"""
        actual = markdown_to_blocks(markdown)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(actual, expected)
    def test_document_to_blocks2(self):
        markdown = """# This is a heading

        

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            * This is the first list item in a list block
            * This is a list item
            * This is another list item
            
            """
        actual = markdown_to_blocks(markdown)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(actual, expected)

class TestBlockIdentify(unittest.TestCase):
    def test_heading(self):
        block = "# This is a heading"
        actual = block_to_block_type(block)
        expected = "heading"
        self.assertEqual(actual, expected)
    def test_heading2(self):
        block = "###### This is a heading"
        actual = block_to_block_type(block)
        expected = "heading"
        self.assertEqual(actual, expected)
    def test_heading3(self):
        block = "####### This is a heading"
        actual = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(actual, expected)
    def test_code(self):
        block = "``` This is some code ```"
        actual = block_to_block_type(block)
        expected = "code"
        self.assertEqual(actual, expected)
    def test_quote(self):
        block = ">This is a quote\n>with 2 lines"
        actual = block_to_block_type(block)
        expected = "quote"
        self.assertEqual(actual, expected)
    def test_quote2(self):
        block = ">This is a quote"
        actual = block_to_block_type(block)
        expected = "quote"
        self.assertEqual(actual, expected)
    def test_unordered(self):
        block = "* This is an unordered list\n- with 2 items"
        actual = block_to_block_type(block)
        expected = "unordered_list"
        self.assertEqual(actual, expected)
    def test_unordered2(self):
        block = "* This is an unordered list"
        actual = block_to_block_type(block)
        expected = "unordered_list"
        self.assertEqual(actual, expected)
    def test_ordered(self):
        block = "1. This is an ordered list\n2. with 2 items"
        actual = block_to_block_type(block)
        expected = "ordered_list"
        self.assertEqual(actual, expected)
    def test_ordered2(self):
        block = "1. This is an ordered list"
        actual = block_to_block_type(block)
        expected = "ordered_list"
        self.assertEqual(actual, expected)
    def test_paragraph(self):
        block = "1. This is nothing in particular\n> It's a mess of stuff"
        actual = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()