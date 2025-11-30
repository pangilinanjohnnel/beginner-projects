operator = input("Select an operator (+ - * /): ")

try:
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
except ValueError:
    print("Error: Please enter only numbers.")
    exit()

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
else:
    print("Operator is not available")


