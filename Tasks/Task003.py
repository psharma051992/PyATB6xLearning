# Write a program to calculate the area of the circle given its radius using the
# ```Area = π * r**2 (Take a pie as 3.14)
import math

# I/P - r -> Float
# O/P - String formatted output of area

# Logic Building Formula
# ---Step 1-----
# Figure out the inputs and output
# input -> r -> float --> Datatype
# pi = 3.14
# power -> pow or **  -> any
# output -> String -> float - area, print_area

radius = float(input("Enter the circle area:\n"))
print(radius)
# area = 3.14987654 * (radius**2)       # There are 2 ways to calculate the area -> One is this
# area = 3.14987654 * (pow(radius, 2))  # second way
area = math.pi * (pow(radius, 2))       # Third way
print("The area of the circle :", area)
# String data formatting
print(f"The area of circle -> {area:.2f}") # F is basically to round off value to decimal points

