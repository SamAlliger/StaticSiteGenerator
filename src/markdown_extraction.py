import re

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def markdown_to_blocks(markdown):
    lines = list(map(str.strip, markdown.split("\n")))
    lines_to_add = ""
    blocks = []
    for i in range(0, len(lines)):
        if lines[i] == "" and lines_to_add == "":
                pass
        elif lines[i] == "":
            blocks.append(lines_to_add)
            lines_to_add = ""
        else:
            if lines_to_add == "":
                lines_to_add = lines[i]
            else:
                lines_to_add = lines_to_add + "\n" + lines[i]
            if i == len(lines) - 1:
                blocks.append(lines_to_add)
    return blocks

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### "), 0, 7):
        return "heading"
    elif block[:3] == "```" and block[-3:] == "```":
        return "code"
    lines = block.split("\n")
    quote_counter = 0
    unordered_counter = 0
    last_ordered = 0
    for line in lines:
        if line[:1] == ">":
            quote_counter += 1
        elif line[:2] in ("* ", "- "):
            unordered_counter += 1
        elif line[:1].isnumeric():
            if line[1:3] == ". " and last_ordered + 1 == int(line[:1]):
                last_ordered = int(line[:1])
    if quote_counter == len(lines):
        return "quote"
    elif unordered_counter == len(lines):
        return "unordered_list"
    elif last_ordered == len(lines):
        return "ordered_list"
    return "paragraph"
