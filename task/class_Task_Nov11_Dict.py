string = 'automation'

char_count = {}

# for char in string:
#     char_count[char] = char_count.get(char,0)+1
#
# print(char_count)


for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)
