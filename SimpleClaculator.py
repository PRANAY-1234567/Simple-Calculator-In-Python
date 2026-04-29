class SimpleCalculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def setData(self, n1, n2):
        self.num1 = n1
        self.num2 = n2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 == 0:
            return "Error: Division by zero"
        return self.num1 / self.num2


# Main program
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

calc = SimpleCalculator()
calc.setData(n1, n2)

print("Addition       :", calc.addition())
print("Subtraction    :", calc.subtraction())
print("Multiplication :", calc.multiplication())
print("Division       :", calc.division())