import unittest
from solution import solve

class TestThresholdStepReducer(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solve([12, 5, 18], 4), [0, 1, 2])

    def test_example_2(self):
        self.assertEqual(solve([3, 2, 1], 5), [3, 2, 1])

    def test_zeros(self):
        self.assertEqual(solve([0, 0, 0], 3), [0, 0, 0])

    def test_exact_multiples(self):
        self.assertEqual(solve([10, 20, 30], 10), [0, 0, 0])

    def test_single_element(self):
        self.assertEqual(solve([7], 3), [1])

if __name__ == '__main__':
    unittest.main()
