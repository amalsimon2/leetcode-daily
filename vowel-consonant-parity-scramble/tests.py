import unittest
from solution import solve

class TestVowelConsonantParityScramble(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solve("algorithm"), "aoilgrthm")

    def test_example_2(self):
        self.assertEqual(solve("python"), "opythn")

    def test_all_vowels(self):
        self.assertEqual(solve("aeiou"), "aeiou")

    def test_all_consonants(self):
        self.assertEqual(solve("bcdfg"), "bcdfg")

    def test_single_char(self):
        self.assertEqual(solve("a"), "a")
        self.assertEqual(solve("b"), "b")

    def test_empty(self):
        self.assertEqual(solve(""), "")

if __name__ == '__main__':
    unittest.main()
