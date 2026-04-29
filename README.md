# 🧮 Simple Calculator in Python (OOP)

## 📌 Description

This Python program implements a **Simple Calculator** using **Object-Oriented Programming (OOP)**. It performs basic arithmetic operations like addition, subtraction, multiplication, and division with proper error handling.

---

## 🚀 Features

* Uses a `SimpleCalculator` class
* Takes user input
* Performs:

  * Addition
  * Subtraction
  * Multiplication
  * Division
* Handles **division by zero** safely

---

## 🛠️ How It Works

1. A class `SimpleCalculator` is created with:

   * `num1`, `num2` as attributes

2. Methods:

   * `setData()` → Assigns input values
   * `addition()` → Returns sum
   * `subtraction()` → Returns difference
   * `multiplication()` → Returns product
   * `division()` →

     * Checks if divisor is `0`
     * Returns error message if true
     * Otherwise performs division

3. In the main program:

   * User inputs two numbers
   * Object is created
   * All operations are performed and printed

---

## 💻 Code

```python id="c9k2pl"
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
```

---

## ▶️ Example Output

```id="x7p4mz"
Enter first number: 10
Enter second number: 5
Addition       : 15.0
Subtraction    : 5.0
Multiplication : 50.0
Division       : 2.0
```

### ❌ Division by Zero Case

```id="m2z8qa"
Enter first number: 10
Enter second number: 0
Division       : Error: Division by zero
```

---

## 📚 Concepts Used

* Class and Object
* Methods
* User input (`input()`)
* Arithmetic operations
* Conditional statements

---

## ⚠️ Issue in Your Code

Your code was **duplicated twice** at the end. It will still run, but it's unnecessary.

👉 Remove the repeated part to keep your code clean.

---

## 🎯 Use Case

This program helps beginners understand:

* How to organize logic using classes
* How to handle runtime errors like division by zero

---

## 🔧 Future Improvements

* Add menu-driven interface
* Handle invalid input (`ValueError`)
* Add power (`**`) and modulus (`%`) operations
* Build GUI calculator (Tkinter)

---

## 📄 License

This project is open-source and free to use.
