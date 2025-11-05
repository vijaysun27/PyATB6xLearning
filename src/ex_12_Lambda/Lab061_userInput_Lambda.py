import math

n = int(input("Enter a number "))

result = lambda n:"Even" if n%2==0 else "Odd"
r=result(n)
print(r)


print (lambda :math.pow(int(input("Enter the number: "))),2) # Less Readability can be replaced with normal functions