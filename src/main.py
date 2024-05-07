from textnode import TextNode
from leafnode import LeafNode
from textnode_functions import *
from block_functions import *

def main():
    text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item
"""
    
    blocks = markdown_to_block(text)
    for block in blocks:
        print("========")
        print(block)



main()

