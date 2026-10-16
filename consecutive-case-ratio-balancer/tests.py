import unittest
from solution import solve

class TestSolve(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solve("aAbBcC"), 6)

    def test_example_2(self):
        self.assertEqual(solve("aAaaBb"), 4)

    def test_all_upper(self):
        self.assertEqual(solve("AAAA"), 0)

    def test_all_lower(self):
        self.assertEqual(solve("aaaa"), 0)

    def test_single_char(self):
        self.assertEqual(solve("a"), 0)

    def test_empty_ratio(self):
        self.assertEqual(solve("aA"), 2)

if __name__ == '__main__':
    unittest.main()
