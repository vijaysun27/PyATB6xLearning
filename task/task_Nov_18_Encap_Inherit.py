'''Build a Test Framework with Encapsulation + Inheritance

🎯 Goal:
Create a simple automation structure that uses:
A BaseTest class for setup/teardown (Parent class)
A LoginTest class that inherits BaseTest (Child class)
Encapsulate sensitive data (like credentials) as private variables

✅ Requirements:

Create a BaseTest class:
Has a protected variable _driver = "Chrome".
Method setup() prints "Launching browser: Chrome".
Method teardown() prints "Closing browser".
Create a LoginTest class that inherits BaseTest:
Has private variables for username and password.
Method run_test() that prints:
"Running login test with user: <username>".
Use encapsulation: access private vars only through a method (e.g., get_user()).

Create an object of LoginTest and call:
setup()
run_test()
teardown()

O/P:
Launching browser: Chrome
Running login test with user: admin
Closing browser'''


class BrowserControl:

    def __init__(self, driver):
        self._driver = driver #Protected variable

    def setup(self):
        return f"Launching Browser: {self._driver}"

    def teardown(self):
        return f"Closing the Browser"


class LoginTest(BrowserControl): # Inherits base class

    def __init__(self, driver, username, password):
        super().__init__(driver)
        self.__username = username #Private variable
        self.__password = password #Private variable

    def run_test(self):
        return f"Running login test with user: {self.__username}"

    def get_username(self):
        return self.__username

p2 = LoginTest("Chrome", "admin", "password123")
print(p2.setup())

p2.get_username()
print(p2.run_test())
print(p2.teardown())
