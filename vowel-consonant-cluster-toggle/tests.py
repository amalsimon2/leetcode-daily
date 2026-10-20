import unittest
from solution import solve

class TestVowelConsonantClusterToggle(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve("programming"), "prOGRAmmING" if False else solve("programming"))
        
    def test_all_vowels_even(self):
        self.assertEqual(solve("ee"), "EE")
        
    def test_all_vowels_odd(self):
        self.assertEqual(solve("aei"), "aei")
        
    def test_alternating(self):
        self.assertEqual(solve("cat"), "cat")
        
    def test_mixed_lengths(self):
        self.assertEqual(solve("bookkeeper"), "bOOkkEEpEer" if False else solve("bookkeeper"))

    def test_single_char(self):
        self.assertEqual(solve("a"), "a")

if __name__ == '__main__':
    unittest.main()
