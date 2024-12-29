from htmlnode import ParentNode
from textnode_conversion import text_to_textnodes
from markdown_extraction import block_to_block_type, markdown_to_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    HTML_Nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        heading_count = block.count("#", 0, 7)
        cleaned_block = clean_block(block, block_type, heading_count)
        children = []
        if block_type == "code":
            children.append(ParentNode("code", text_to_children(cleaned_block)))
        elif block_type in ("unordered_list", "ordered_list"):
            items = cleaned_block.split("\n")
            for item in items:
                children.append(ParentNode("li", text_to_children(item)))
        else:
            children = text_to_children(cleaned_block)
        HTML_Nodes.append(ParentNode(block_type_to_tag(block_type, heading_count), children))
    return ParentNode("div", HTML_Nodes)

def block_type_to_tag(block_type, heading_count=0):
    if block_type == "heading":
        return f"h{heading_count}"
    elif block_type == "code":
        return "pre"
    elif block_type == "quote":
        return "blockquote"
    elif block_type == "unordered_list":
        return "ul"
    elif block_type == "ordered_list":
        return "ol"
    elif block_type == "paragraph":
        return "p"
    else:
        raise Exception("Not a valid block type!")

def clean_block(block, block_type, heading_count=0):
    clean_block = ""
    if block_type == "heading":
        clean_block = block.replace(pad_character("#", heading_count) + " ", "", 1)
    elif block_type == "code":
        clean_block = block.replace("```", "")
    elif block_type == "quote":
        clean_block = block.replace(">", "", 1).replace("\n>", "\n")
    elif block_type == "unordered_list":
        if block.startswith("* "):
            clean_block = block.replace("* ", "", 1).replace("\n* ", "\n").replace("\n- ", "\n")
        else:
            clean_block = block.replace("- ", "", 1).replace("\n* ", "\n").replace("\n- ", "\n")
    elif block_type == "ordered_list":
        items = block.split("\n")
        cleaned_items = []
        for item in items:
            cleaned_items.append(item[3:])
        clean_block = "\n".join(cleaned_items)
    elif block_type == "paragraph":
        clean_block = block
    else:
        raise Exception("Not a valid block type!")
    return clean_block

def pad_character(character, count):
    i = 0
    padded = ""
    for i in range(0, count):
        padded = padded + character
        i += 1
    return padded

def text_to_children(text):
    Text_Nodes = text_to_textnodes(text)
    Leaf_Nodes = []
    for node in Text_Nodes:
        Leaf_Nodes.append(node.text_node_to_html_node())
    return Leaf_Nodes