# Creating a python script that defines and uses functions to perform basic operations.
# Defining Functions
def add_numbers(x,y):
    result = (x + y)
    return result
def subtract_numbers(x,y):
    result = (x-y)
    return result
def multiply_numbers(x,y):
    result = (x * y)
    return result

def divide_numbers(numerator, denominator):
    if denominator == 0:
        return None
    else:
        return numerator/denominator

# Step 2: Defining my list
num_list = [6,8,10]

# Step 3: Performing operation using defined function and loops.
for num in num_list:
    add_result = add_numbers(x=num, y=2)
    sub_result = subtract_numbers(x=num,y=2)
    mul_result = multiply_numbers(x=num, y=2)
    div_result= divide_numbers(numerator=num, denominator=2)
    print(f"{num},{2}")
    print(f" Add:{add_result}, Subtract:{sub_result}, Multiply:{mul_result}, Division:{div_result}")
















