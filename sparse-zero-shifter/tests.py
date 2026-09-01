import unittest
from solution import solve

class TestSparseZeroShifter(unittest.TestCase):
    def test_example_1(self):
        arr = [0, 1, 0, 3, 12]
        self.assertEqual(solve(arr), [1, 3, 12, 0, 0])

    def test_example_2(self):
        arr = [0, 0, 1]
        self.assertEqual(solve(arr), [1, 0, 0])

    def test_no_zeros(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(solve(arr), [1, 2, 3, 4])

    def test_all_zeros(self):
        arr = [0, 0, 0]
        self.assertEqual(solve(arr), [0, 0, 0])

    def test_single_element(self):
        arr = [0]
        self.assertEqual(solve(arr), [0])

if __name__ == '__main__':
    unittest.main()
