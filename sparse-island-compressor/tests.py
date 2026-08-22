import unittest
from solution import solve


class TestSparseIslandCompressor(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solve([0, 3, 0, 1, 4, 0, 2]), [3, 1, 4, 2, 0, 0, 0])

    def test_example_2(self):
        self.assertEqual(solve([0, 0, 0]), [0, 0, 0])

    def test_no_zeros(self):
        self.assertEqual(solve([1, 2, 3]), [1, 2, 3])

    def test_all_zeros_at_end(self):
        self.assertEqual(solve([5, 4, 0, 0]), [5, 4, 0, 0])

    def test_single_element(self):
        self.assertEqual(solve([0]), [0])
        self.assertEqual(solve([7]), [7])


if __name__ == '__main__':
    unittest.main()
