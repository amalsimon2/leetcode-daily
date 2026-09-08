import unittest
from solution import solve

class TestSubarrayCapBoundedProduct(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve([2, 1, 3, 2], 2), 4)

    def test_all_valid(self):
        self.assertEqual(solve([1, 2, 2], 3), 6)

    def test_all_invalid(self):
        self.assertEqual(solve([5, 6, 7], 3), 0)

    def test_single_element_valid(self):
        self.assertEqual(solve([4], 5), 1)

    def test_single_element_invalid(self):
        self.assertEqual(solve([6], 5), 0)

    def test_alternating(self):
        self.assertEqual(solve([1, 5, 2, 5, 1], 3), 3)

if __name__ == '__main__':
    unittest.main()
