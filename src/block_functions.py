from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

class BlockType:
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"

def markdown_to_block(markdown):
    markdown_split = markdown.split("\n\n")
    markdown_blocks = []
    for md in markdown_split:
        md = md.strip()
        if len(md) != 0:
            markdown_blocks.append(md)
    return markdown_blocks

def block_to_block_type(block):
    start = block.split(' ', 1)[0]
    if len(start) <= 6 and len(start[0].strip('#')) == 0:
        return BlockType.heading

    if block.startswith("```") and block.endswith("```"):
        code_split = block.split("```")
        if len(code_split) == 3 and len(code_split[0]) == 0 and len(code_split[2]) == 0:
            return BlockType.code

    quote = True
    for line in block.split('\n'):
        if not line.startswith("> "):
            quote = False
            break
    if quote:
        return BlockType.quote
    
    unordered_list = True
    for line in block.split('\n'):
        if not line.startswith("* ") and not line.startswith("- "):
            unordered_list = False
            break
    if unordered_list:
        return BlockType.unordered_list

    ordered_list = True
    splited_block = block.split('\n')
    for i in range(len(splited_block)):
        if not splited_block[i].startswith(f"{i+1}. "):
            ordered_list = False
            break
    if ordered_list:
        return BlockType.ordered_list

    return BlockType.paragraph
        

def markdown_to_html_node(markdown):
    html_node = ParentNode(tag="div", children=[], props=None)
    html_node.children = []
    markdown_blocks_types = []
    markdown_blocks = markdown_to_block(markdown)
    for md_block in markdown_blocks:
        markdown_blocks_types.append((md_block, block_to_block_type(md_block)))
    
    for block, block_type in markdown_blocks_types:
        html_block = None
        if block_type == BlockType.quote:
            html_block = quote_block_to_node(block)
        elif block_type == BlockType.unordered_list:
            html_block = unordered_list_block_to_node(block)
        elif block_type == BlockType.ordered_list:
            html_block = ordered_list_block_to_node(block)
        elif block_type == BlockType.code:
            html_block = code_block_to_node(block)
        elif block_type == BlockType.heading:
            html_block = heading_block_to_node(block)
        elif block_type == BlockType.paragraph:
            html_block = paragraph_block_to_node(block)
        else:
            raise Exception("Unknown Block Type")
        html_node.children.append(html_block)
    return html_node


def quote_block_to_node(block):
    quotes = "\n"
    for b in block.split("\n"):
        quotes += "\n" + b[1:].strip()
    return LeafNode(tag="blockquote", value=quotes[1:])

def unordered_list_block_to_node(block):
    block_node = ParentNode(tag="ul", children=[])
    block_node.children = []
    for line in block.split('\n'):
        block_node.children.append(
                LeafNode(tag="li", value=line[1:].strip())
                )
    return block_node

def ordered_list_block_to_node(block):
    block_node = ParentNode(tag="ol", children=[])
    block_node.children = []
    for line in block.split('\n'):
        block_node.children.append(
                LeafNode(tag="li", value=line[2:].strip())
                )
    return block_node
    

def code_block_to_node(block):
    block_node = ParentNode(tag="pre",
                        children=[
                            LeafNode(tag="code", value=block.strip("`"))
                            ]
                            )
    return block_node

def heading_block_to_node(block):
    l = len(block.split(' ', 1)[0])
    return LeafNode(tag=f"h{l+1}", value=block[l:].strip())

def paragraph_block_to_node(block):
    return LeafNode(tag="p", value=block)




