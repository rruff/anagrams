import unittest
from anagrams import utils

class TestUtils(unittest.TestCase):
    def test_sort_chars(self):
        chars = utils.sort_chars('odor')
        self.assertEqual('door', chars)
        
        chars = utils.sort_chars('stag')
        self.assertEqual('agst', chars)

    def test_sort_chars_empty_returns_empty_string(self):
        chars = utils.sort_chars('')
        self.assertEqual('', chars)

    def test_sort_chars_string_is_none_return_none(self):
        chars = utils.sort_chars(None)
        self.assertEqual(None, chars)

if __name__ == '__main__':
    unittest.main()