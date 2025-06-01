import unittest
from markdown_to_htmlnode import markdown_to_htmlnode

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """
> Once more unto the breach!
> Hit and run, rhymes with **grug** B)
"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        
        self.assertEqual(
            html,
            "<div><blockquote>Once more unto the breach! Hit and run, rhymes with <b>grug</b> B)</blockquote></div>",
        )

    def test_heading(self):
        md = """
### this is an _h3_ heading
now with more text!
"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><h3>this is an <i>h3</i> heading\nnow with more text!</h3></div>"
        )

    def test_ul(self):
        md = """
- this is item one
- this is the item after item one
"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ul><li>this is item one</li><li>this is the item after item one</li></ul></div>",
        )

    def test_ol(self):
        md = """
1. this is _item_ one
2. this is the **item** after item one
"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ol><li>this is <i>item</i> one</li><li>this is the <b>item</b> after item one</li></ol></div>",
        )

if __name__ == "__main__":
    unittest.main()