# Task to do - a 3 input from the user
# and perform all mathematical operations
# Do add, sub, mul and division

num1 = float(input("Enter a first number: "))
num2 = float(input("Enter a second number: "))
num3 = float(input("Enter a third number: "))

# Performing opeartions
sum_result = num1 + num2 + num3  #add all three numbers
sub_result = num1 - num2 - num3  #subtract second no.from first and subtract third no. from 2nd no.
print(sum_result)
print(sub_result)

mul_result = num1 * num2 * num3 #multiply all three numbers
print(mul_result)

div_result = (num1 / num2) / num3  #divide all three numbers
print(div_result)