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
