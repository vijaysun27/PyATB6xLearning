# def first_non_repeating(string):
#     for char in string:
#         if string.count(char)==1:
#             return char
#     return None
#
# result1=first_non_repeating("swiss")
# print(f"The first non repeating character in the string is '{result1}'")
# result=first_non_repeating("annusinha")
# print(f"The first non repeating character in the string is '{result}'")

# squares = {x**2 for x in range(5)}
# print(squares)

squares = []

for i in range(1,6):
    #i**2
    squares.append(i**2)
print(squares)

square_set = set(squares)
print(type(square_set))

#
