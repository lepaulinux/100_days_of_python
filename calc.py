def calculate(n1, n2, operation):
    if operation == "+":
        return n1 + n2
    elif operation == "-":
        return n1 - n2
    elif operation == "*":
        return n1 * n2
    elif operation == "/":
        return n1 / n2 if n2 != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"

# Define allowed operations
values = ["+", "-", "*", "/"]

# Get user input and convert to numbers
v1 = float(input("Type value 1: "))
v2 = float(input("Type value 2: "))

# Get operation and validate
op = input("What operation do you want to do? (+, -, *, /): ")
if op not in values:
    print("Invalid operation selected!")
else:
    # Perform calculation
    result = calculate(v1, v2, op)
    print(f"Result: {result}")
