import unittest
from solution import solve

class TestPicketFenceAlternator(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(solve([1, 5, 2, 8, 3]))

    def test_example_2(self):
        self.assertTrue(solve([1, 3, 2, 4]))

    def test_example_3(self):
        self.assertFalse(solve([1, 2, 3]))

    def test_two_elements_valid(self):
        self.assertTrue(solve([10, 5]))
        self.assertTrue(solve([5, 10]))

    def test_two_elements_zero_diff(self):
        self.assertFalse(solve([5, 5]))

    def test_flat_spot_middle(self):
        self.assertFalse(solve([1, 5, 5, 8]))

    def test_long_alternating(self):
        self.assertTrue(solve([2, 5, 1, 9, 3, 7, 4]))

if __name__ == '__main__':
    unittest.main()
