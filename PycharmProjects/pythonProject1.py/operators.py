# Creating a profit & Loss Calculator for my product

buying_price = float(input('Enter product price: $' ))
selling_price = int(input('Enter selling price: $' ))

profit = selling_price - buying_price
loss = buying_price - selling_price

if selling_price > buying_price:
    print(f"Profit was made")
else:
    print(f"Loss was made")

