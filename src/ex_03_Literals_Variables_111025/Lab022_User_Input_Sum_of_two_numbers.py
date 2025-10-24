# Logic Building
from numbers import Complex

# Step 1
# I/P -> num1, num2  -> int
# O/P -> sum, mul, div, sub -> What is the datatype of output (Always ask from interviewer) -> float

# Step 2 - Rough logic

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
# result will not be print in the addition of 2 numbers, to get the result converts inputs to float
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)