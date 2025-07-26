ProductPrice = {}

while True:
    entry = input("Enter the Product and Price of this : ")

    if entry.lower() == "done":
        break

    if "," in entry:
        product, price = entry.split(",", 1)
        product = product.strip()
        price = price.strip()
        try:
            ProductPrice[product] = float(price)
        except ValueError:
            print(f"Invalid price format for '{product}'. Please enter a valid number.")
    else:
        print("Invalid number is 'product, price'.")

print("\nProduct and Price List:")
for product, price in ProductPrice.items():
    print(f"{product}: {price}")