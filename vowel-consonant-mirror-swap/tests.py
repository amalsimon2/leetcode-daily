import unittest
from solution import solve

class TestVowelConsonantMirrorSwap(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solve("leetcode"), "leotcede")

    def test_example_2(self):
        self.assertEqual(solve("hello"), "holle")

    def test_no_vowels(self):
        self.assertEqual(solve("rhythm"), "rhythm")

    def test_only_vowels(self):
        self.assertEqual(solve("aeiou"), "uoiea")

    def test_single_character(self):
        self.assertEqual(solve("a"), "a")
        self.assertEqual(solve("b"), "b")

    def test_alternating(self):
        self.assertEqual(solve("abcde"), "ebcda")

if __name__ == '__main__':
    unittest.main()
