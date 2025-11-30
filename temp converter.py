unit = input("Celsius or Fahrenheit (C/F): ").upper()

try:
    temp = float(input("Enter temperature: "))
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

if unit == "C":
    temp = (9 * temp) / 5 + 32
    print(f"Temperature in Fahrenheit is: {temp:.1f}F")
elif unit == "F":
    temp = (temp - 32) * 5 / 9
    print(f"Temperature in Celsius is: {temp:.1f}C")
else:
    print("Unit is invalid")
