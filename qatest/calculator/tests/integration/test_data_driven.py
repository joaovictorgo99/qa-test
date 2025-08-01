import json
import unittest

from qatest.calculator.my_calculator.my_calculator import my_calculator

class Entries:
    def __init__(self, id, operation, x, y):
        self.id = id
        self.operation = operation
        self.x = x
        self.y = y

class App:
    def __init__(self, database):
        with open(database) as f:
            data = json.load(f)

        self.entries = [Entries(**item) for item in data]

    def get_entry(self, id):
        for entry in self.entries:
            if entry.id == id:
                return entry

class TestBasic(unittest.TestCase):
    def setUp(self):
        self.app = App(database="qatest/calculator/tests/integration/fixtures/test_data.json")

    def test_entry_count(self):
        self.assertEqual(len(self.app.entries), 100)

    def test_existence_of_entry(self):
        entry = self.app.get_entry(76)
        self.assertEqual(entry.operation, "div")
        self.assertEqual(entry.x, 3.5)
        self.assertEqual(entry.y, 99)

class TestComplex(unittest.TestCase):
    def setUp(self):
        self.app = App(database="qatest/calculator/tests/integration/fixtures/test_data.json")

    def test_add(self):
        entry = self.app.get_entry(67)
        result = my_calculator(entry.operation, entry.x, entry.y)
        self.assertEqual(result, 7)

    def test_subtract(self):
        entry = self.app.get_entry(54)
        result = my_calculator(entry.operation, entry.x, entry.y)
        self.assertEqual(result, -5)

    def test_multiply(self):
        entry = self.app.get_entry(68)
        result = my_calculator(entry.operation, entry.x, entry.y)
        self.assertEqual(result, 0)

    def test_divide(self):
        entry = self.app.get_entry(21)
        result = my_calculator(entry.operation, entry.x, entry.y)
        self.assertEqual(result, 11)

    def test_invalid_operation(self):
        entry = self.app.get_entry(56)
        result = my_calculator(entry.operation, entry.x, entry.y)
        self.assertEqual(result, "error: Invalid operation")

    def test_invalid_number(self):
        with self.assertRaises(TypeError):
            entry = self.app.get_entry(61)
            result = my_calculator(entry.operation, entry.x, entry.y)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            entry = self.app.get_entry(2)
            result = my_calculator(entry.operation, entry.x, entry.y)

if __name__ == '__main__':
    unittest.main()
