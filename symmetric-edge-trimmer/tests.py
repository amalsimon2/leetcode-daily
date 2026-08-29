import unittest
from solution import solve

class TestSymmetricEdgeTrimmer(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solve([3, 2, 3, 4, 3, 3], 3), 3)

    def test_example_2(self):
        self.assertEqual(solve([5, 5, 5], 5), 0)

    def test_no_match(self):
        self.assertEqual(solve([1, 2, 3], 5), 3)

    def test_empty_array(self):
        self.assertEqual(solve([], 1), 0)

    def test_single_element_match(self):
        self.assertEqual(solve([7], 7), 0)

    def test_single_element_no_match(self):
        self.assertEqual(solve([7], 4), 1)

if __name__ == '__main__':
    unittest.main()
