import unittest
from solution import solve

class TestSolve(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(solve("aAABbbcc"), "L1U3L4")

    def test_single_char_lower(self):
        self.assertEqual(solve("a"), "L1")

    def test_single_char_upper(self):
        self.assertEqual(solve("Z"), "U1")

    def test_all_lower(self):
        self.assertEqual(solve("abcde"), "L5")

    def test_all_upper(self):
        self.assertEqual(solve("ABCDE"), "U5")

    def test_alternating(self):
        self.assertEqual(solve("aBaB"), "L1U1L1U1")

if __name__ == '__main__':
    unittest.main()
