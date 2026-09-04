import unittest
from solution import solve

class TestStrideElementCollector(unittest.TestCase):
    
    def test_example_one(self):
        self.assertEqual(solve([10, 20, 30, 40, 50, 60], 1, 2), [20, 40, 60])

    def test_example_two(self):
        self.assertEqual(solve([5, 4, 3, 2, 1], 0, 3), [5, 2])

    def test_start_out_of_bounds_implicitly_handled_if_valid_by_constraint(self):
        self.assertEqual(solve([7], 0, 5), [7])

    def test_large_stride(self):
        self.assertEqual(solve([1, 2, 3, 4, 5], 2, 10), [3])

    def test_unit_stride(self):
        self.assertEqual(solve([1, 2, 3], 0, 1), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
