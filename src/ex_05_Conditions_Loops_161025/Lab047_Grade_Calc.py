# Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (eg. A,B,C,D or F)
# based on following grading scale
# from selectors import SelectSelector

# A :90-100
# B :80-89
# C :70-79
# D: 60-69
# F: 0-59

# Logic building formula

# I/P : User Input -score -> Int
# O/P : -> str -> A, B

score = int(input("Enter your score: ").strip())

if score > 100 or score <=-1:
    print("You  are Superman!!,you can't get grade")
else:
    if score >= 90 and score <= 100:
        print("Your Grade is A")
    elif score >= 80 and score <= 89:
        print("Your Grade is B")
    elif score >= 70 and score <= 79:
        print("Your Grade is C")
    elif score >= 60 and score <= 69:
        print("Your Grade is D")
    else:
        print("Your Grade is F")

# float, abc - try catch

