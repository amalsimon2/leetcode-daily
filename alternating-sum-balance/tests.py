import unittest
from solution import solve

class TestAlternatingSumBalance(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solve([2, -1, 2]), 1)

    def test_example_2(self):
        self.assertEqual(solve([1, 2, 3]), -1)

    def test_single_element(self):
        self.assertEqual(solve([5]), 0)

    def test_no_match(self):
        self.assertEqual(solve([1, 1, 1, 1]), -1)

if __name__ == '__main__':
    unittest.main()
