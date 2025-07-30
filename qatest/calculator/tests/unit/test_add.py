import unittest

from qatest.calculator.my_calculator.add import add

class TestAdd(unittest.TestCase):
    def test_int(self):
        result = add(1, 1)
        self.assertEqual(result, 2)

    def test_float(self):
        result = add(5.0, 0.7)
        self.assertEqual(result, 6)

    def test_string(self):
        result = add("10", "10")
        self.assertEqual(result, 20)

    def test_negative(self):
        result = add(-1, -1)
        self.assertEqual(result, -2)

if __name__ == "__main__":
    unittest.main()
