import unittest
from solution import solve

class TestStableSensorTrough(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solve([4, 7, 2, 7, 4, 9, 4]), 7)

    def test_example_2(self):
        self.assertEqual(solve([1, 2, 3, 5]), -1)

    def test_all_same(self):
        self.assertEqual(solve([5, 5, 5, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(solve([-3, -1, -3, -5, -1]), -1)

    def test_single_element(self):
        self.assertEqual(solve([10]), -1)

if __name__ == '__main__':
    unittest.main()
