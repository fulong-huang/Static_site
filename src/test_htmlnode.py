
import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("tag", "value", "child", "props")
        print(node)


if __name__ == "__main__":
    unittest.main()

