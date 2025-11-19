a = {1,2,3}
b = {3,4,5}
#c = a.union(b)
c=a|b

print(c)

#d = a.intersection(b)
d = a&b
print(d)

print(a.difference(b))
print(b.difference(a))

print(a^b)
print(a.symmetric_difference(b))