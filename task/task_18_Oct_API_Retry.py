# Question 2 :
#
# An API sometimes fails due to network delays.
# Write a program to retry the API call 3 times until the response code becomes 200.
# If it still fails after 3 tries, print a failure message.
#
# Hint: Use a while loop with a counter.
# Hint: Use a while loop with a counter.
#
# Expected Output Example:
# Attempt 1: Response 500
# Attempt 2: Response 200



count=1
while count<=3:
    response_code = int(input("Enter a API response code: "))
    if response_code == 200:
        print(f"Attempt {count}: Response {response_code}")
        break
    else:
        print(f"Attempt {count}: Response {response_code}")
    count+=1

print(18*'*')
if response_code == 200:
    print("✅ Test Passed")
else:
    print("❌ Test Failed")