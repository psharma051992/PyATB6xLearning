# Write a program to find the max between two

# Logic building formula
# 1 .user inputs -> two integers or float as well
# 2. o/p -> int 1 which ever is greater max number it will return
# 31.4 or 45.34 -float

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

if num1 >= num2:                   # num1 == num2 will be handled by equal to operator with >
    print("Number1 is maximum:", num1)
else:
    print("Number2 is maximum:", num2)

# if num1 > 0 and num2 >0 :            # This condition only requires if ask by interviewer
#    print("The number should be positive")

