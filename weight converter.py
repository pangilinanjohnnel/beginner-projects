try:
    weight = float(input("Enter your weight: "))
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

unit = input("Kilograms or Pounds? (K/L): ").upper()

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "kg"
else:
    print(f"{unit} is not a valid unit.")
    exit()

print(f"Your weight is {weight:.2f} {unit}")
