# Task for the today (14-oct-25)
# Take 2 inputs from the user
# Print the quotient and remainder
# 20 -> num1
# 3 -> num2
# Q -> 6
# R -> 2

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

quotient = num1 // num2    #// gives the quotient and its new type operator in Python only not in java
remainder = num1 % num2    #// this will give the remainder

print(quotient)
print(remainder)
