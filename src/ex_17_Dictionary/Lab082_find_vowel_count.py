input_string = "hello, world"

#a,e,i,o,u

vowels="aeiou"

vowels_count = 0
result=list()

for char in input_string:
    if char in vowels:
        vowels_count = vowels_count+1
        result.append(char)

print(result)
print(vowels_count)
