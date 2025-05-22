import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a link node", TextType.LINK)
        node2 = TextNode("This is a second link node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_texttype(self):
        node = TextNode("testing...", TextType.BOLD)
        node2 = TextNode("testing...", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("testing...", TextType.BOLD, "https://goon.org")
        node2 = TextNode("testing...", TextType.BOLD, "https://edge.gov")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("testing...", TextType.BOLD, "https://edge.gov")
        node2 = TextNode("testing...", TextType.BOLD, "https://edge.gov")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()