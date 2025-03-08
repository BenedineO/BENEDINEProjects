# Python program to calculate total fuel cost for a trip.

# Get User input
distance = float(input("Enter the distance of trip in kilometers: "))
cost_per_litre = float(input("Enter cost per litre of fuel: "))

#  Calculating fuel required
fuel_required = (distance/100) * 8

# Calculating total cost
total_cost = fuel_required * cost_per_litre

# Displaying total cost using f-strings
print(f"Total cost of fuel: {total_cost} Naira.")






