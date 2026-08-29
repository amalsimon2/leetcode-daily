import unittest
from solution import solve

class TestAdjacentPolarityInterleave(unittest.TestCase):
    def test_example_1(self):
        nums = [3, -1, 2, -5]
        expected = [3, -1, 2, -5]
        self.assertEqual(solve(nums), expected)

    def test_example_2(self):
        nums = [-2, 3, 1, -1]
        expected = [-2, 3, -1, 1]
        self.assertEqual(solve(nums), expected)

    def test_all_neg_first(self):
        nums = [-5, -2, 4, 3]
        expected = [-5, 4, -2, 3]
        self.assertEqual(solve(nums), expected)

    def test_minimal(self):
        nums = [1, -1]
        expected = [1, -1]
        self.assertEqual(solve(nums), expected)

if __name__ == '__main__':
    unittest.main()
