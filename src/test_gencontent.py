from gencontent import extract_title
from gencontent import generate_page
import unittest

class TestInlineMarkdown(unittest.TestCase):

    def test_extract_title(self):
        title = extract_title("# Hello")
        test_title = "Hello"
        self.assertEqual(test_title,title)
        
    def test_extract_title_none(self):
        with self.assertRaises(Exception):
            extract_title("No title here")