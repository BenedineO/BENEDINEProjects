def list_items(*args):
    print("Items List")
    """Displays list of items
    """
    for item in args:
        print(f"- {item}")


# Calling the function
list_items("Garri", "Fish", "Bread", "Milk")


# ------------------------------------------------------------------------------------------

def largest_number(*number):
    return max(number)


# Calling my function
number = largest_number(20, 30, 50, 60, 70, 31, 45)
print(f"The Largest Number is: {number}")


# ------------------------------------------------------------------------------------------

def any_number(*numbers):
    return sum(numbers)


# Calling my function
number_2 = any_number(20, 30, 50, 60, 70, 31, 45)
print(f"The Total Number is: {number_2}")


# -------------------------------------------------------------------------------------------

def list_of_numbers(*args):
    for number in args:
        if number % 2 == 0:
            print(f'Even Numbers are: {number}')


# Calling my function
list_of_numbers(20, 30, 50, 60, 70, 31, 45)

# ------------------------------------------------------------------------------------------