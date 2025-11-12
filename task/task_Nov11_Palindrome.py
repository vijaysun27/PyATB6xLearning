#Question - ✅Palidrome of String

def check_palindrome(string):
    string1=string.lower()
    if string1.isalpha():
        if string1[::-1]==string1:
            return f"'{string}' is a Palindrome String."
        else:
            return f"'{string}' is not Palindrome String."
    else:
        return f"String is Invalid, enter a valid string from a-z/A-Z."

input_string = input("Enter a string: ").strip()
result = check_palindrome(input_string)
print(result)


