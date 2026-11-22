def shopping_cart(**products):
 total = 0
 for product, price in products.items():
    print(product, ": ", price)
 total += price
 print("Total: ", total)

shopping_cart(apple=15, orange=12, mango=10)
