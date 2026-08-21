import unittest
from solution import solve

class TestVowelVanguardShift(unittest.TestCase):
    def test_single_vowel(self):
        self.assertEqual(solve(['p', 'y', 't', 'h', 'o', 'n']), ['p', 'y', 't', 'h', 'o', 'n'])

    def test_multiple_vowels(self):
        self.assertEqual(solve(['a', 'b', 'e', 'c', 'i']), ['i', 'b', 'a', 'c', 'e'])

    def test_no_vowels(self):
        self.assertEqual(solve(['b', 'c', 'd', 'f']), ['b', 'c', 'd', 'f'])

    def test_all_vowels(self):
        self.assertEqual(solve(['a', 'e', 'i']), ['i', 'a', 'e'])

    def test_mixed_case(self):
        self.assertEqual(solve(['A', 'b', 'E', 'c']), ['E', 'b', 'A', 'c'])

if __name__ == '__main__':
    unittest.main()
