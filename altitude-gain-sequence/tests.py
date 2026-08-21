import unittest
from solution import solve

class TestAltitudeGain(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(solve([-5, 1, 5, 0, -7]), 1)

    def test_example_two(self):
        self.assertEqual(solve([4, -3, 2, -2]), 4)

    def test_all_negative(self):
        self.assertEqual(solve([-1, -2, -3]), 0)

    def test_all_positive(self):
        self.assertEqual(solve([1, 2, 3]), 6)

    def test_single_element(self):
        self.assertEqual(solve([5]), 5)
        self.assertEqual(solve([-5]), 0)

if __name__ == '__main__':
    unittest.main()
