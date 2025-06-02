import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test1(self):
        md = """
> this is not the header

## this is a header

# this is the correct header
"""
        header = extract_title(md)

        self.assertEqual(header, "this is the correct header")

    def test1(self):
        md = """
# header header header

> quote quote quote

```swag```
"""
        header = extract_title(md)

        self.assertEqual(header, "header header header")



if __name__ == "__main__":
    unittest.main()