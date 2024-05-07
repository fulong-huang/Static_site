
import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                    ],
                )
        print("_______PARENT+________")
        print(node.to_html())
        print("_______PARENT+________")


if __name__ == "__main__":
    unittest.main()

