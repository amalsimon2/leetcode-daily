import unittest
from solution import solve

class TestConsecutiveFrequencyTrimmer(unittest.TestCase):
    def test_example(self):
        nums = [1, 1, 2, 2, 2, 3, 1, 1]
        k = 2
        expected = [1, 1, 2, 2, 2, 1, 1]
        self.assertEqual(solve(nums, k), expected)

    def test_all_removed(self):
        nums = [1, 2, 3, 4]
        k = 2
        expected = []
        self.assertEqual(solve(nums, k), expected)

    def test_all_kept(self):
        nums = [5, 5, 5, 5]
        k = 2
        expected = [5, 5, 5, 5]
        self.assertEqual(solve(nums, k), expected)

    def test_empty_array(self):
        nums = []
        k = 3
        expected = []
        self.assertEqual(solve(nums, k), expected)

    def test_single_element(self):
        nums = [7]
        k = 1
        expected = [7]
        self.assertEqual(solve(nums, k), expected)

if __name__ == '__main__':
    unittest.main()
