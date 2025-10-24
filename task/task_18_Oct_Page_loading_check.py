# Question 3 :
# Simulate a page loading check using a while loop.
# If page_loaded becomes True within 5 seconds, print success; else timeout.
#
# Hint: Use a counter (like wait_time) and break condition.

wait_time = 1

while wait_time<=5:
    is_page_loaded = input("Is the page loaded (true/false)? ").strip()
    if is_page_loaded.lower() == "true":
        print(f"Page loaded in {wait_time} seconds")
        break
    wait_time+=1

print(20*'*')
if is_page_loaded.lower()=="true":
    print("Success")
else:
    print("Session Timed Out")
