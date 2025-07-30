import unittest

from qatest.calculator.my_calculator.multiply import multiply

class TestMultiply(unittest.TestCase):
    def test_int(self):
        result = multiply(9, 9)
        self.assertEqual(result, 81)

    def test_float(self):
        result = multiply(9.9, 9.9)
        self.assertEqual(result, 98)

    def test_string(self):
        with self.assertRaises(TypeError):
            result = multiply("10", "10")

    def test_negative(self):
        result = multiply(-1, -1)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()
