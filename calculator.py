# Function Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Main Program
try:
    print("Operations: add, subtract, multiply, divide")
    op = input("Enter operation: ").lower().strip()
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if op == "add":
        print(f"Result: {add(num1, num2)}")
    elif op == "subtract":
        print(f"Result: {subtract(num1, num2)}")
    elif op == "multiply":
        print(f"Result: {multiply(num1, num2)}")
    elif op == "divide":
        try:
            result = divide(num1, num2)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
    else:
        print("Invalid operation selected!")

except ValueError:
    print("Error: Please enter valid numbers only!")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")