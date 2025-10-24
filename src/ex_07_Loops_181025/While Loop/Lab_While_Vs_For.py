# A Program based on Interview Question -->  While Verses For loop

test_id = 0
while test_id < 10:
    print("Running the test ID number:",test_id)
    test_id = test_id + 1      # test_id += 1

# Above same code with For loop

for test_id in range(0, 10,1):
    print("Test with for loop")
    print("Running the test ID number:",test_id)