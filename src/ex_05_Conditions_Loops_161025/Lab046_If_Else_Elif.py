# Find the maximum between 3 numbers

# Logic building Formula
# User inputs -num1 ,num2 ,num3 ->int
# o/p ->int or string with max number

num1 = int(input("Enter the first number\n"))  # 5 , #10
num2 = int(input("Enter the second number\n"))  # 3 ,#12
num3 = int(input("Enter the third number\n"))  # 2 ,#11

# Rough Logic
# 5 > 3 and 5 > 2 ->5
# num1 > num2 and num1 > num3 -> num1
# num2 > num1 and num2 > num3 -> num2
# num3 -> max
"""
# Final Code
if num1 > num2 and num1 > num3:
    print("Max number1 is:", num1)
elif num2 > num3 and num2 > num1:
    print("Max number2 is:", num2)
else:
    print("Max number3 is:", num3)
"""
# Still in above code, there are issues, lets says if num1 and num2 are equal and
# if num3 is smaller even then give output that num3 is max
# Fix for above final code is as follows:

if num1 >= num2 and num1 >= num3:
    print("Max number1 is:", num1)
elif num2 >= num3 and num2 >= num1:
    print("Max number2 is:", num2)
else:
    print("Max number3 is:", num3)
