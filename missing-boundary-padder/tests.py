import unittest
from solution import solve

class TestMissingBoundaryPadder(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(solve([4, 1, 7, 7, 3]), [2, 5, 6])

    def test_no_missing(self):
        self.assertEqual(solve([1, 2, 3, 4]), [])

    def test_single_element(self):
        self.assertEqual(solve([10]), [])

    def test_duplicates_only(self):
        self.assertEqual(solve([5, 5, 5]), [])

    def test_negative_numbers(self):
        self.assertEqual(solve([-3, 0, -1]), [-2])

if __name__ == '__main__':
    unittest.main()
