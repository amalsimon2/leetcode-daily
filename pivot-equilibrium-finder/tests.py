import unittest
from solution import solve

class TestPivotEquilibriumFinder(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(solve([1, 7, 3, 6, 5, 6]), 3)

    def test_example_two(self):
        self.assertEqual(solve([1, 2, 3]), -1)

    def test_single_element(self):
        self.assertEqual(solve([5]), 0)

    def test_left_edge_equilibrium(self):
        self.assertEqual(solve([0, 1, -1]), 0)

    def test_right_edge_equilibrium(self):
        self.assertEqual(solve([1, -1, 0]), 2)

    def test_zeros(self):
        self.assertEqual(solve([0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()
