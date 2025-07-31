import unittest

from qatest.calculator.my_calculator.my_calculator import my_calculator

class TestMyCalculator(unittest.TestCase):
    def test_add(self):
        result = my_calculator("+", 5, 8)
        self.assertEqual(result, 13)

    def test_subtract(self):
        result = my_calculator("-", 13, 8)
        self.assertEqual(result, 5)

    def test_multiply(self):
        result = my_calculator("*", 2, 4)
        self.assertEqual(result, 8)

    def test_divide(self):
        result = my_calculator("/", 4, 2)
        self.assertEqual(result, 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            result = my_calculator("/", 4, 0)

    def test_invalid_operation(self):
        result = my_calculator("%", 4, 0)
        self.assertEqual(result, "error: Invalid operation")

if __name__ == '__main__':
    unittest.main()
