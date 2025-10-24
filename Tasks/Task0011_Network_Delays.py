"""
An API sometimes fails due to network delays.
Write a program to retry the API call 3 times until the response code becomes 200.
If it still fails after 3 tries, print a failure message.
Hint: Use a while loop with a counter.
Hint: Use a while loop with a counter.
Expected Output Example:
Attempt 1: Response 500
Attempt 2: Response 200
✅ Test Passed
❌ Test Failed
"""
attempt = 1

while attempt <= 3:
    num = int(input(f"Attempt {attempt}: Enter response code (200 or 500): "))
    if num == 200:
        print("✅ Test Passed")
        break
    else:
        print("Error code 500, Page load failed")
    attempt += 1

if num != 200:
    print("❌ Test Failed")

