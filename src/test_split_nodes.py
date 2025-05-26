import unittest

from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
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

class TestSplitImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])        
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_2(self):
        node = TextNode(
            "This is text with ![image1](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("image1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )

    def test_split_links_2(self):
        node = TextNode(
            "This is text with [link1](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )

    def test_split_images_3(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ],
            new_nodes,
        )

    def test_split_links_3(self):
        node = TextNode(
            "[link](https://i.imgur.com/zjjcJKZ.png)[second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png")
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()