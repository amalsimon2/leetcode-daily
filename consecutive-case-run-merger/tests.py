import unittest
from solution import solve

class TestConsecutiveCaseRunMerger(unittest.TestCase):
    
    def test_basic(self):
        self.assertEqual(solve("aAABbbcc"), "L1U3L4")

    def test_all_lowercase(self):
        self.assertEqual(solve("abcde"), "L5")

    def test_all_uppercase(self):
        self.assertEqual(solve("ABCDE"), "U5")

    def test_alternating(self):
        self.assertEqual(solve("aAbBcC"), "L1U1L1U1L1U1")

    def test_single_character(self):
        self.assertEqual(solve("X"), "U1")
        self.assertEqual(solve("x"), "L1")

if __name__ == '__main__':
    unittest.main()
