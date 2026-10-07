import unittest
from solution import solve

class TestVowelConsonantBracketInverter(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solve("abc"), "(a)[b][c]")

    def test_example_2(self):
        self.assertEqual(solve("aeiou"), "(a)(e)(i)(o)(u)")

    def test_all_consonants(self):
        self.assertEqual(solve("bcd"), "[b][c][d]")

    def test_single_vowel(self):
        self.assertEqual(solve("e"), "(e)")

    def test_single_consonant(self):
        self.assertEqual(solve("z"), "[z]")

if __name__ == '__main__':
    unittest.main()
