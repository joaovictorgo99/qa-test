import unittest

from qatest.calculator.my_calculator.subtract import subtract

class TestSubtract(unittest.TestCase):
    def test_int(self):
        result = subtract(1, 1)
        self.assertEqual(result, 0)

    def test_float(self):
        result = subtract(5, 0.7)
        self.assertEqual(result, 4)

    def test_string(self):
        with self.assertRaises(TypeError):
            result = subtract("10", "10")

    def test_negative(self):
        result = subtract(-1, -1)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()
