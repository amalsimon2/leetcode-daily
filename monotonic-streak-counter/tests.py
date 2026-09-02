import unittest
from solution import solve

class TestMonotonicStreakCounter(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(solve([1, 2, 3, 2, 1, 4, 5]), 3)

    def test_example_two(self):
        self.assertEqual(solve([5, 5, 5, 5]), 1)

    def test_single_element(self):
        self.assertEqual(solve([42]), 1)

    def test_strictly_increasing(self):
        self.assertEqual(solve([1, 2, 3, 4, 5]), 5)

    def test_strictly_decreasing(self):
        self.assertEqual(solve([5, 4, 3, 2, 1]), 5)

    def test_mixed_streaks(self):
        self.assertEqual(solve([10, 20, 15, 10, 5, 8, 12]), 4)

if __name__ == '__main__':
    unittest.main()
