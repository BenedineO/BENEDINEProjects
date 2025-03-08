# Creating my script of list and tuples
names = ["Caleb", "Ben", "Sarah", "Phil", "Ric"]
ages = [10,20,30,40,50]
countries = ["Nigeria", "Kenya", "Namibia", "Ghana", "Uganda"]
allowed_countries = ("Kenya", "Nigeria", "South Africa")

# Check if country of the last person is in the list of the allowed countries
if countries[-1] in allowed_countries_tuple:
    print(f" {names[-1]} is from an allowed country")
    number_from_allowed_countries = 1
    number_from_not_allowed_countries = 0
else:
    print(f" {names[-1]} is not from an allowed country")
    number_from_allowed_countries = 0
    number_from_not_allowed_countries = 1



# Printing Summary Message
total_checked = 1
print("\nsummary:")
print(f"total people checked:{total_checked}")
print(f"number from allowed countries = {number_from_allowed_countries}")
print(f"number from not allowed countries = {number_from_not_allowed_countries}")






