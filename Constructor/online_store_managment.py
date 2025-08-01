class Product:
    def __init__(self, product_name, price, stock):
        self.product_name = product_name
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f"Product Name: {self.product_name}, Price: {self.price}, Stock: {self.stock}")

    def update_price(self, new_price):
        print(f"Updating price to {new_price}...")
        self.price = new_price
        print(f"New Price: {self.price}")

    def update_stock(self, new_stock):
        print(f"Updating stock to {new_stock}...")
        self.stock = new_stock
        print(f"New Stock: {self.stock}")


# Take input from the user
product_name = input()
initial_price = float(input())
initial_stock = int(input())

new_price = float(input())
new_stock = int(input())

# Create Product instance with initial values
product = Product(product_name, initial_price, initial_stock)

# Display the product info
product.display_info()

# Take updated price and stock as input


# Update product details
product.update_price(new_price)
product.update_stock(new_stock)
