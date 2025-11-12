#Question - ✅Palidrome of String

def check_palindrome(string):
    string=string.lower()
    if string.isalpha():
        if string[::-1]==string:
            return f"'{string}' is a Palindrome String."
        else:
            return f"'{string}' is not Palindrome String."
    else:
        return f"String is Invalid, enter a valid string from a-z/A-Z."

input_string = input("Enter a string: ")
result = check_palindrome(input_string)
print(result)


