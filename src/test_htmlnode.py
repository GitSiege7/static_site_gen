import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_constructor(self):
        node = HTMLNode("p", "this is a value", None, {"href": "https://www.google.com"})
        test_string = "HTMLNode(p, this is a value, None, {'href': 'https://www.google.com'})"
        self.assertEqual(node.__repr__(), test_string)

    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com"})
        test_string = " href=\"https://www.google.com\""
        self.assertEqual(node.props_to_html(), test_string)

    def test_props_to_html_2(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        test_string = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), test_string)


if __name__ == "__main__":
    unittest.main()