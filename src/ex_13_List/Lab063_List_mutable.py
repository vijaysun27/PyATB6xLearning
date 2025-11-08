# List is an ordered collection and supports modification(mutable)

my_list = [1,2,True,'pramod',12.34]

# my_list[0] = "Pramod"
# my_list[1] = "Dutta"
# print(my_list)
#
# for item in my_list:
#     print(item)
#
#
# # range() also returns the list
#
# for i in range(1,5):
#     print(i)

# append()

my_list = [1,2,True,'pramod',12.34]
my_list.append(5)
print(my_list)

#extend()
my_list.extend([7,8,9])
print(my_list)

#insert()
my_list.insert(1,"Dutta")
print(my_list)
print(len(my_list))

#copy()
my_copy_list = my_list.copy()
print(my_copy_list)

#remove()
my_copy_list.remove("Dutta")
print(my_copy_list)

#pop()








