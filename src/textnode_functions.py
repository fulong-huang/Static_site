
import re
from textnode import TextNode
from leafnode import LeafNode

class TextType:
    text = "text"
    bold = "bold"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"

def text_node_to_html_node(text_node):
    leafNode = None
    if text_node.text_type == TextType.text:
        leafNode = LeafNode(value=text_node.text)
    elif text_node.text_type == TextType.bold:
        leafNode = LeafNode(value=text_node.text, tag='b')
    elif text_node.text_type == TextType.italic:
        leafNode = LeafNode(value=text_node.text, tag='i')
    elif text_node.text_type == TextType.code:
        leafNode = LeafNode(value=text_node.text, tag='code')
    elif text_node.text_type == TextType.link:
        leafNode = LeafNode(value=text_node.text, tag='a')
    elif text_node.text_type == TextType.image:
        leafNode = LeafNode(value=text_node.text, tag='img')
    else:
        raise Exception("Text node contains invalid type")
    return leafNode

def _split_node_delimiter(old_node, delimiter, text_type):
    new_nodes = []
    old_text = old_node.text
    split_text = old_text.split(delimiter)
    
    for i in range(len(split_text)):
        if i % 2 == 0:
            new_nodes.append(
                    TextNode(
                        text      = split_text[i],
                        text_type = old_node.text_type
                        )
                    )
        else:
            new_nodes.append(
                    TextNode(
                        text      = split_text[i],
                        text_type = text_type
                        )
                    )

    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        new_nodes += _split_node_delimiter(node, delimiter, text_type)
    return new_nodes

def _split_node_image(old_node):
    new_nodes = []
    curr_text = old_node.text
    images = extract_markdown_images(curr_text)
    for img in images:
        split_text = curr_text.split(f"![{img[0]}]({img[1]})", 1)
        if len(split_text[0]) != 0:
            new_nodes.append(
                    TextNode(text=split_text[0], text_type=old_node.text_type)
                    )
        new_nodes.append(
                TextNode(text=img[0], text_type=TextType.image, url=img[1])
                )
        curr_text = split_text[1]
    if len(curr_text) != 0:
        new_nodes.append(
                TextNode(text=curr_text, text_type=old_node.text_type)
                )
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes += _split_node_image(node)
    return new_nodes

def _split_node_link(old_node):
    new_nodes = []
    curr_text = old_node.text
    links = extract_markdown_links(curr_text)
    for link in links:
        split_text = curr_text.split(f"[{link[0]}]({link[1]})", 1)
        if len(split_text[0]) != 0:
            new_nodes.append(
                    TextNode(text=split_text[0], text_type=old_node.text_type)
                    )
        new_nodes.append(
                TextNode(text=link[0], text_type=TextType.link, url=link[1])
                )
        curr_text = split_text[1]
    if len(curr_text) != 0:
        new_nodes.append(
                TextNode(text=curr_text, text_type=old_node.text_type)
                )
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes += _split_node_link(node)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def text_to_textnodes(text):
    nodes = [TextNode(text=text, text_type=TextType.text)]
    nodes = split_nodes_delimiter(nodes, "*", TextType.italic)
    nodes = split_nodes_delimiter(nodes, "**", TextType.bold)
    nodes = split_nodes_delimiter(nodes, "`", TextType.code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

