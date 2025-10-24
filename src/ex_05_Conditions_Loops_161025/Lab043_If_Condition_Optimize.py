# Write a program to take a user age and let him know that he can go to club or not.
# age = 21

# Logic Building formula
# ---- Step 1 ----
# I/P - age, int
# O/P - String (result) -> He can go to club or not

# ---Step 3 ---- Write the logic
age = int(input("Enter the age\n").strip()) # strip() will remove the leading and trailing spaces
if age <=0 or age > 130:
    print("Please enter a valid age")
else:
    if age >= 21:
       print("Yes, You can go to club")
    else:
       print("No, You can't go to club")

# ---- Step 4 ---- Check for edge cases
# we should consider edge cases such as:
# Negative ages or extremely high values --> Program will break
# Non-numeric input - ABC
# Age which is valid. > 130

# ---- Step 5 ---- Optimize the code
# Handle all the edges

