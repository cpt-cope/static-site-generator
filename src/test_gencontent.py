import unittest
from gencontent import extract_title

class TestGenContent(unittest.TestCase):
    
    def test_extract_title(self):
        markdown = """
# My Page Title

Some paragraph text here.
"""
        title = extract_title(markdown)
        self.assertEqual(title, "My Page Title")

    def test_spaced_out_title(self):
        markdown = """
#     Spaced Out Title

More content below.
"""
        title = extract_title(markdown)
        self,self.assertEqual(title, "Spaced Out Title")

    def test_middle_header(self):
        markdown = """
This paragraph comes first.

# Later Title

More text.
"""
        title = extract_title(markdown)
        self.assertEqual(title, "Later Title")

    def test_not_main_header(self):
        markdown = """
## Section Title

### Smaller Section
"""
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_no_header(self):
        markdown = """
Just a paragraph.

- A list item
- Another list item
"""
        with self.assertRaises(Exception):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()