import unittest
from solution import solve

class TestCaseClusterInverter(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve("AbC-dEfG!HI"), "ABC-defg!HI")

    def test_all_lower(self):
        self.assertEqual(solve("hello world"), "hello world")

    def test_all_upper(self):
        self.assertEqual(solve("PYTHON CODE"), "PYTHON CODE")

    def test_mixed_tie(self):
        # 1 upper, 1 lower -> not strictly upper > lower -> becomes lower
        self.assertEqual(solve("Ab"), "ab")

    def test_mixed_strictly_upper(self):
        # 2 upper, 1 lower -> strictly upper > lower -> becomes upper
        self.assertEqual(solve("ABc"), "ABC")

    def test_symbols_and_numbers(self):
        self.assertEqual(solve("123-AbC_xyz!99"), "123-ABC_xyz!99")

    def test_single_char(self):
        self.assertEqual(solve("A"), "A")
        self.assertEqual(solve("x"), "x")
        self.assertEqual(solve("-"), "-")

if __name__ == '__main__':
    unittest.main()
