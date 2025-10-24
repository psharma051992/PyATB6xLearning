# IIn automation, you often compare expected and actual outputs.
# #Write code to check if a test case passed or failed.
# #expected_title = "Dashboard"
# #actual_title = "Dashboard "

# #✅ Test Passed – Title matches

# #True - why >  Strip and convert them into the lowercase = both of them are equal.

# Logic Building Formula

# User I/P - String
# O/P - String
# expected_title = "Dashboard"  # We can check the result by this way as well- 1st way
# actual_title = "Dashboard"

actual_title = input("Enter actual title: ")      # we can use strip and lower here as well
expected_title = input("Enter expected title: ")

if expected_title.strip().lower() == actual_title.strip().lower():  #strip used to remove extra spaces
    print("Title Matches")
else:
    print("Title Does Not Match")
