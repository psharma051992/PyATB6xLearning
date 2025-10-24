# Check if the user can log in based on correct username and password.
# I/p - String
# username = "admin"
# password = "1234"

# O/p - String
# ✅ Login Successful
# For the Fail condition Other = ❌ Invalid Credentials

username = input("Enter username:\n").strip()
password = input("Enter password:\n").strip()

if username.lower() == "admin" and password == "12345":
    print("✅ User logged in successfully or Login Successful")
else:
    print("Invalid Credentials")