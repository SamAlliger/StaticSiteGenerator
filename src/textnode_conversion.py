from textnode import TextNode, TextType
from markdown_extraction import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes=[]
    for node in old_nodes:
        if node.text_type != TextType.normal:
            new_nodes.append(node)
        elif len(node.text.split(delimiter)) % 2 == 0:
            raise Exception("Invalid Markdown syntax")
        else:
            split_nodes = node.text.split(delimiter)
            for i in range(0, len(split_nodes)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_nodes[i], TextType.normal))
                else:
                    new_nodes.append(TextNode(split_nodes[i], text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.normal or extract_markdown_images(node.text) == []:
                new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            text_to_split = node.text
            for image in images:
                split_text = text_to_split.split(f"![{image[0]}]({image[1]})", 1)
                if split_text == []:
                    pass
                else:
                        new_nodes.append(TextNode(split_text[0], TextType.normal))
                        text_to_split = text_to_split.replace(split_text[0], "", 1)
                new_nodes.append(TextNode(image[0], TextType.image, image[1]))
                text_to_split = text_to_split.replace(f"![{image[0]}]({image[1]})", "", 1)
            if text_to_split != "":
                 new_nodes.append(TextNode(text_to_split, TextType.normal))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.normal or extract_markdown_links(node.text) == []:
                new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            text_to_split = node.text
            for link in links:
                split_text = text_to_split.split(f"[{link[0]}]({link[1]})", 1)
                if split_text == []:
                    pass
                else:
                        new_nodes.append(TextNode(split_text[0], TextType.normal))
                        text_to_split = text_to_split.replace(split_text[0], "", 1)
                new_nodes.append(TextNode(link[0], TextType.link, link[1]))
                text_to_split = text_to_split.replace(f"[{link[0]}]({link[1]})", "", 1)
            if text_to_split != "":
                 new_nodes.append(TextNode(text_to_split, TextType.normal))
    return new_nodes

def text_to_textnodes(text):
    nodes = TextNode(text, TextType.normal)
    return split_nodes_image(split_nodes_link(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter([nodes],"**", TextType.bold), "*", TextType.italic),"`", TextType.code)))

