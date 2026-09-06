import unittest
from solution import solve

class TestElementFrequencyRank(unittest.TestCase):
    def test_example(self):
        nums = [4, 2, 4, 3, 2, 4]
        # Counts: {4: 3, 2: 2, 3: 1}
        # Freqs: [1, 2, 3]
        # Ranks: freq 1 -> 1, freq 2 -> 2, freq 3 -> 3
        # Output: [3, 2, 3, 1, 2, 3]
        self.assertEqual(solve(nums), [3, 2, 3, 1, 2, 3])

    def test_single_element(self):
        self.assertEqual(solve([5]), [1])

    def test_all_same(self):
        self.assertEqual(solve([7, 7, 7, 7]), [1, 1, 1, 1])

    def test_all_unique(self):
        nums = [1, 2, 3]
        self.assertEqual(solve(nums), [1, 1, 1])

if __name__ == '__main__':
    unittest.main()
