original_price = float(input("Enter a item price:-"))
market_price = int(input("Enter discount price:-"))

discount = (market_price / 100) * original_price
final_amount = original_price - discount

print(f"The final price of the item is {discount}% discount after", final_amount)