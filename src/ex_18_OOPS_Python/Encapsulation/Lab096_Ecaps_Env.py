from dotenv import load_dotenv
import os

load_dotenv()

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):

        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        #load_dotenv()
        if self.email == os.getenv("VMO_USERNAME") and self.password == os.getenv("VMO_PASSWORD"):
            print("Allowed, Login Success")
        else:
            print("Login Failed")


email = input("Enter the vwo login email ")
password = input("Enter the vwo login password ")

vwo_object_ref = VWOLoginPage(email,password)
vwo_object_ref.login_confirm()

print(os.name)
print("Loaded username:", os.getenv("USERNAME"))
print("Loaded password:", os.getenv("PASSWORD"))
