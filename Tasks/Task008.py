# You want to check whether a web page loads within 3 seconds (performance test condition).
# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds

# Logic Building Formula

# User I/P - float
# O/P - String

load_time = float(input("The web page load time in seconds \n"))

if load_time <= 0:
    print("⚠️ Invalid input: load time must be greater than 0 seconds")
elif load_time <= 3:
    print(f"✅ Page loaded successfully in {load_time} seconds")
else:
    print(f"⚠️ Page load too slow: {load_time} seconds")

# Another Way of writing the code
"""
if load_time > 3:
    print("The web page load time is more than 3 seconds")
elif load_time == 3:
    print("The web page loads within 3 seconds")
else:
    print("The web page load time is lesser than 3 seconds")
"""