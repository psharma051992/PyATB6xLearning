# Write a program where You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.

# I/P response = 404 , O/P ❌ Failed API Request
# I/P response = 200 , O/P ✅ Passed API Request

#Logic Building Formula
# User Inputs - Int
# O/P - String

response = int(input("The Api response is \n"))

if response == 200:
    print("API response is successful")
elif response == 404:
    print("API response is unsuccessful")
else:
    print("Please enter a valid response")
