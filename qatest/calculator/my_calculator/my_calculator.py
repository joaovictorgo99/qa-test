from qatest.calculator.my_calculator.add import add
from qatest.calculator.my_calculator.divide import divide
from qatest.calculator.my_calculator.multiply import multiply
from qatest.calculator.my_calculator.subtract import subtract

def my_calculator(operation, x, y):
    if operation == "+":
        return add(x, y)
    elif operation == "-":
        return subtract(x, y)
    elif operation == "*":
        return multiply(x, y)
    elif operation == "/":
        return divide(x, y)
    else:
        return "error: Invalid operation"
