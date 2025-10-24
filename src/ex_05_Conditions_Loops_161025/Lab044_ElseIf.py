# Find the number is even or odd
num = int(input("Please enter a number: ").strip())

if num >= 0:
    if num % 2 == 0:
        print("The number is even")
    else:                                # we can convert this if else part into one line i.e one-liner conditions
        print("The number is odd")
else:
    print("Negative number")

# ------
# You can write short one-liner condition using ternary operator

if num >= 0:
    print("Even" if num % 2 == 0 else "Odd")
else:
    print("Negative number")

