import unittest

from qatest.calculator.my_calculator.divide import divide

class TestDivide(unittest.TestCase):
    def test_int(self):
        result = divide(12, 4)
        self.assertEqual(result, 3)

    def test_float(self):
        result = divide(10, 0.3)
        self.assertEqual(result, 33)

    def test_string(self):
        with self.assertRaises(TypeError):
            result = divide("10", "10")

    def test_negative(self):
        result = divide(-1, -1)
        self.assertEqual(result, 1)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            result = divide(5, 0)

if __name__ == "__main__":
    unittest.main()
