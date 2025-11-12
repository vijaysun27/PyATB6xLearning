dict_1 = {'a': 10, 'b':20,'c':30,'d':30}
#
# def max_value(dict_1):
#     #return max(dict_1.values())
#     return max(dict_1.keys())
#
# print(max_value(dict_1))

# Remove duplicates values

unique_value = set()
result = {}

for key,value in dict_1.items():
    if value not in unique_value:
        result[key] = value
        unique_value.add(value)
print(result)