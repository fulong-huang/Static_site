import unittest

from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        print("LEAF=============")
        node = LeafNode("p", "This is a paragraph of text.")
        print(node.to_html())
        print("LEAF=============")
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(node.to_html())

if __name__ == "__main__":
    unittest.main()

