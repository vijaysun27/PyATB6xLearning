# Q - You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.

response_code = int(input("Enter the response code: "))

if response_code == 404:
    print(f"Status code is {response_code}. API Request Failed")
elif response_code == 200:
    print(f"Status code is {response_code}. API Request Passed")
else:
    print("Invalid Status code")


# Q2
#
# In automation, you often compare expected and actual outputs.
# Write code to check if a test case passed or failed.
#
# expected_title = "Dashboard"
# actual_title = "Dashboard "

act_title = input("Enter the title: ").strip()
ex_title = "Dashboard"

if act_title.lower()==ex_title.lower():
    print("Title Matches. Tests are passed")
else:
    print("Title mis-match. Tests are failed")


# Q3
#
# You want to check whether a web page loads within 3 seconds (performance test condition).
#
# load_time = 4.2
# Page load too slow: 4.2 seconds

page_load_time = float(input("Enter the page load time: "))

if page_load_time <= 3:
    print("The page load time is under 3 seconds, thus meeting the performance requirements")
elif page_load_time>3:
    print(f"Page load time is slow, it's more than 3 seconds.")
else:
    print("Enter valid time in seconds")

# Q4 Check if the user can log in based on correct username and password.

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "1234":
        print("Login Successful")
else:
    print("Invalid Username or Password")
