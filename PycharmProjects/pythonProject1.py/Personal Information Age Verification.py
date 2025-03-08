# Creating a python script that uses lists, loops, and conditional statements to verify and categorize personal information based on age.

# Step 1: Defining my Data
names = ["Ben", "Charles", "Sarah","Phil", "Ric"]
ages = [35,40, 38, 27, 16]
age_threshold = 18    # minimum age for a specific benefit


# Step 2: Checking age and categorizing
for i in range(5):
    name = names[i]
    age = ages [i]

    if age >= age_threshold:
        print(f"{name} is eligible.")
    else:
        print(f"{name} is not eligible.")


# Step 3: Print Processing Message
for name in names:
    print(f"processing {name}...")
