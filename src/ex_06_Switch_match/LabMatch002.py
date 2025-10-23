print("Enter the test name which you would like to run")
test_type = input("Pick a test type only from these API/UI/Performance/Security: ")

match test_type:

    case "API":
        print("We are running a POSTMAN API Testcase.")
    case "UI":
        print("We are running a Selenium Testcase.")
    case "Performance":
        print("We are running a Performance Testcase.")
    case "Security":
        print("We are running a Security Testcase.")
    case _:
        print("Invalid Type")