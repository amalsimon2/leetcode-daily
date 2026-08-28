import unittest
from solution import solve

class TestArrayParityBoundary(unittest.TestCase):
    def test_mixed_elements(self):
        nums = [3, 1, 2, 4]
        self.assertEqual(solve(nums), [2, 4, 3, 1])

    def test_all_odds(self):
        nums = [1, 3, 5]
        self.assertEqual(solve(nums), [1, 3, 5])

    def test_all_evens(self):
        nums = [2, 4, 6]
        self.assertEqual(solve(nums), [2, 4, 6])

    def test_single_element(self):
        nums = [7]
        self.assertEqual(solve(nums), [7])

    def test_empty_or_alternating(self):
        nums = [1, 2, 3, 4, 5, 6]
        self.assertEqual(solve(nums), [2, 4, 6, 1, 3, 5])

if __name__ == '__main__':
    unittest.main()
