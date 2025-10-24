# Given a number you need to calculate the factorial of that number
# n = 5
# Fact = 5×4×3*2*1 = 120
# Fact = 0 → 1

# Logic Building Formula
# User I/P -> Int
# O/P -> String

num = int(input("Enter a number: "))
fact = 1
i = 1
if num < 0:
    print("Factor cannot be negative.")
elif num == 0:
    print("Factor cannot be zero or factorial of 0 is 1.")
else:
    while i <= num:
        fact = fact * i
        i += 1
    print("The factorial of",num,"is",fact)

