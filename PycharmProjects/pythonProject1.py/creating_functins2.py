# Creating a function to calculate total price
def cal_total(price, quantity):
    """Creating a function t calculate total of a product"""

    total = price * quantity
    print(f"The total price is N{total}")

# Calling the Function
cal_total(200, 5)