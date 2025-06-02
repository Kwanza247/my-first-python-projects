# Simple Calculator in Python

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

print("Select operation: +, -, *, /")
operation = input("Operation: ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if operation == '+':
    print("Result:", add(a, b))
elif operation == '-':
    print("Result:", subtract(a, b))
elif operation == '*':
    print("Result:", multiply(a, b))
elif operation == '/':
    print("Result:", divide(a, b))
else:
    print("Invalid operation")

