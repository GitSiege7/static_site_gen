import unittest

from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        
        textnode1 = TextNode("This is text with a ", TextType.TEXT)
        textnode2 = TextNode("code block", TextType.CODE)
        textnode3 = TextNode(" word", TextType.TEXT)
        
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), [textnode1, textnode2, textnode3])

    def test_italic(self):
        node1 = TextNode("I love _pizza_", TextType.TEXT)
        node2 = TextNode("This is text with an _italic_ word", TextType.TEXT)

        textnode1 = TextNode("I love ", TextType.TEXT)
        textnode2 = TextNode("pizza", TextType.ITALIC)
        textnode3 = TextNode("This is text with an ", TextType.TEXT)
        textnode4 = TextNode("italic", TextType.ITALIC)
        textnode5 = TextNode(" word", TextType.TEXT)

        self.assertEqual(split_nodes_delimiter([node1, node2], "_", TextType.ITALIC), [textnode1, textnode2, textnode3, textnode4, textnode5])


if __name__ == "__main__":
    unittest.main()