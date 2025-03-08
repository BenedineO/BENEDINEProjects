# --------------------GROUP 1-----------------------------
# CLASS EXERCISE ON EVENT ACCESS
# Writing a python script that determines members access to event.

# Defining Variables based on age, membership and invitation
age = int(input("Enter your age: "))
is_member = input("Do you have membership? (yes/no): ")
has_invitation = input("Do you have an invitation? (yes/no): ")

# Creating a boolean expression for membership and invitation
is_member = is_member == "yes"
has_invitation = has_invitation == "yes"

# Using Logical operators to determine access and print messages for different events.
if is_member and age >= 18:
    print("Access to Member's Event")
elif has_invitation or age >= 21:
    print("Access to VIP Event")
elif is_member and has_invitation:
    print("Access to Exclusive Event")
else:
    print("Access to General Event")


# ---------------------THANK YOU-----------------------------








