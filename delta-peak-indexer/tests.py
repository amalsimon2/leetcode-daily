import unittest
from solution import solve

class TestDeltaPeakIndexer(unittest.TestCase):
    
    def test_standard_peak(self):
        self.assertEqual(solve([1, 3, 2, 4, 1]), 1)
        
    def test_multiple_peaks_returns_first(self):
        self.assertEqual(solve([1, 5, 2, 6, 1]), 1)

    def test_no_peak_decreasing(self):
        self.assertEqual(solve([5, 4, 3, 2, 1]), -1)

    def test_no_peak_increasing(self):
        self.assertEqual(solve([1, 2, 3, 4, 5]), -1)

    def test_short_array(self):
        self.assertEqual(solve([1, 2]), -1)
        self.assertEqual(solve([1]), -1)

    def test_plateau_not_peak(self):
        self.assertEqual(solve([1, 2, 2, 1]), -1)

if __name__ == '__main__':
    unittest.main()
