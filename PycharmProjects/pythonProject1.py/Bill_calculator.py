def calculate_bill(price, quantity, discount =  ):  # Defining my function
    total_cost = price * quantity
    return total_cost  # Returning the output so i can call it anytime


# Providing arguments for output
electricity = calculate_bill(205, 30)
water = calculate_bill(70, 30)
internet = calculate_bill(1000, 30)

# Printing my output in readable format using f-string
if calculate_bill() > 100:
    print(f"Eligible for a 10% discount ₦{electricity + water + internet}!")
else:
    print(f"Total Bill Amount = ₦{electricity + water + internet}")

