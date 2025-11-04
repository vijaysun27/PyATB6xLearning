# def greet_user(n):
#     print(f"Hi {n}")
#
# greet_user("Vijay")
# greet_user("Guru")

#Using return
# def sum_funct(a,b,c):
#     return a+b+c
#
# t = sum_funct(4,5,6)
# print(t)

# Default Variable
# def greet_with_default_param(name="QA"):
#     print("Hi, ", name)
# greet_with_default_param(name="smirit")
# greet_with_default_param()

#Function return multiple values

# def mul_math_op(a,b):
#     return a+b, a-b, a*b
# sum,sub,mul = mul_math_op(19,39)
# print(f"Sum is {sum}")
# print(f"Sub is {sub}")
# print(f"Mul is {mul}")

# Function with Keyword Argument

# def user_detail(name="dhoni",role="WK"):
#     print(f"Hi {name}! you are selected as {role}")
#
# user_detail("Vijay","SDET")
# user_detail(role="DS",name="Guru")
# user_detail() # Default Argument


# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
#
# def sum_of_three(n1=100,n2=200,n3=300):
#     return n1+n2+n3
#
# result = sum_of_three(num1,num2,num3)
# result1=sum_of_three()
# result2=sum_of_three(n1=10)
# result3=sum_of_three(n1=10,n2=30)
# result4=sum_of_three(n1=10,n2=30,n3=40)
# result5=sum_of_three(n1=10,n2=30,n3=num3)
#
# print(result)
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)


a1 = int(input("Enter a: "))
b1 = int(input("Enter b: "))

def sum_of_two(a=10,b=10):
    return a+b

r = sum_of_two(a1,b1)
print(r)
