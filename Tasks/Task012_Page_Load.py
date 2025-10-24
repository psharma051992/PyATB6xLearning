"""
Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.

Hint: Use a counter (like wait_time) and break condition.
"""
import random
import time

wait_time = 0
page_loaded = False

while wait_time < 5:
    # Simulate whether the page loads (randomly True or False)
    page_loaded = random.choice([True, False])
    print(f"Checking... {wait_time + 1} second(s) passed")

    if page_loaded:
        print("✅ Page loaded successfully!")
        break

    # Wait for 1 second before next check
    time.sleep(1)
    wait_time += 1

if not page_loaded:
    print("❌ Timeout! Page did not load in 5 seconds.")

