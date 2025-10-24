# Question 1. :
# Given a Number a number you need to calculate the factorial of that number
# n = 5
# Fact = 5×4×3*2*1 = 120
# Fact = 0 → 1,

n = int(input("Enter a number: "))
fact=1
if n<1:
    print("Enter number greater than 0")
elif n==1:
    print(f"Factorial of {n} is {n}")
else:
    for i in range(1,n+1):
        fact = fact*i
    print(f"Factorial of {n} is {fact}")