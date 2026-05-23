items=[]
prices=[]
total=0

while True:
    item=input("Enter item to buy (q to quit): ")
    if item.lower() =="q":
        break
    else:
        price=float(input(f"Enter the price of {item}: P"))
        items.append(item)
        prices.append(price)

print("-----YOUR CART-----")

for item in items:
    print(item)

for price in prices:
    total += price

print(f"Your total is: P{total}")