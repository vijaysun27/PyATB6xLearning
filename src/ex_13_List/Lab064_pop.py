my_list = [1, 2, True, 'pramod', 12.34, 5, 7, 8, 9]
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(1)
print(my_list)

my_list.clear()
print(my_list)

my_list = [1, 2, True, 'pramod', 12.34, 5, 7, 8, 9]
print(my_list.index(2))

my_list.reverse()
print(my_list)

numbers = [10,20,30,44,55,67,89.99,1001.432,8765]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#Slicing

print(numbers[1:4])
print(numbers[-1])

print("apple" in numbers)
print(20 in numbers)

#List Creation and Comprehension

l=list(range(1,5))
print(l)

#nested lists
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])

#delete()
del numbers[0]
print(numbers)

