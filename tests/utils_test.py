import unittest
from anagrams import utils

class TestUtils(unittest.TestCase):
    def test_sort_chars(self):
        chars = utils.sort_chars('door')
        self.assertEqual('door', chars)
        
        chars = utils.sort_chars('stag')
        self.assertEqual('agst', chars)

if __name__ == '__main__':
    unittest.main()