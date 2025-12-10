menu = {"burger": 80,
    "fries": 50,
    "soft drink": 35,
    "ice cream": 40,
    "chicken nuggets": 60}

order = []
total_price = 0

food = input("Enter the food you want to order (q to quit): ").lower()

while food != "q":
    if food in menu:
        price = menu[food]
        order.append((food, price))
        total_price += price
        print(f"You ordered {food} - ₱{price}")
    else:
        print("Item not in menu. Try again.")

    food = input("Enter the food you want to order (q to quit): ").lower()

print("----- FOOD RECEIPT -----")
for item, price in order:
    print(f"{item} - ₱{price}")

print(f"TOTAL PRICE: ₱{total_price}")


