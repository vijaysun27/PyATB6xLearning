# Question - ✅ Count vowels and consonants in a String

def count_vowels_const(string):
    vowels = 'aeiouAEIOU'
    vowel_count=[]
    const_count=[]
    for char in string:
        if char.isalpha():
            if char in vowels:
                vowel_count.append(char)
            else:
                const_count.append(char)
        else:
            return f"String is Invalid, enter a valid string from a-z/A-Z"
    return f"The vowel count is {len(vowel_count)} and consonents count is {len(const_count)}"

input_string = input("Enter a string: ").strip()
vowels_const_count = count_vowels_const(input_string)
print(vowels_const_count)