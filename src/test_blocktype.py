import unittest

from blocktype import block_to_block_type, BlockType

class TestBlockType(unittest.TestCase):
    def test_blocktype_p(self):
        block = "this is a paragraph block"

        type = block_to_block_type(block)

        self.assertEqual(type, BlockType.PARAGRAPH)

    def test_blocktype_h(self):
        block = "# this is a heading"

        type = block_to_block_type(block)

        self.assertEqual(type, BlockType.HEADING)

    def test_blocktype_h6(self):
        block = "###### this is a heading"

        type = block_to_block_type(block)

        self.assertEqual(type, BlockType.HEADING)

    def test_blocktype_code(self):
        block = "```this is a code block```"

        type = block_to_block_type(block)

        self.assertEqual(type, BlockType.CODE)

    def test_blocktype_quote(self):
        block = "> this is a quote block"

        type = block_to_block_type(block)

        self.assertEqual(type, BlockType.QUOTE)

    def test_blocktype_ulist(self):
        block = "- this is an unordered list\n- this is the second line"

        type = block_to_block_type(block)

        self.assertEqual(type, BlockType.ULIST)

    def test_blocktype_olist(self):
        block = "1. this is an ordered list\n2. this is the second line"

        type = block_to_block_type(block)

        self.assertEqual(type, BlockType.OLIST)


if __name__ == "__main__":
    unittest.main()