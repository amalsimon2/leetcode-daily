import unittest
from solution import solve

class TestTroughPointCounter(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solve([3, 1, 4, 1, 5]), 2)

    def test_example_2(self):
        self.assertEqual(solve([2, 2, 2]), 0)

    def test_single_element(self):
        self.assertEqual(solve([10]), 1)

    def test_two_elements_strict(self):
        self.assertEqual(solve([5, 2]), 1)

    def test_two_elements_equal(self):
        self.assertEqual(solve([3, 3]), 0)

    def test_multiple_troughs(self):
        self.assertEqual(solve([5, 1, 5, 1, 5]), 2)

    def test_strictly_decreasing(self):
        self.assertEqual(solve([5, 4, 3, 2, 1]), 1)

    def test_strictly_increasing(self):
        self.assertEqual(solve([1, 2, 3, 4, 5]), 1)

if __name__ == '__main__':
    unittest.main()
