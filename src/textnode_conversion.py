from textnode import TextNode, TextType

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