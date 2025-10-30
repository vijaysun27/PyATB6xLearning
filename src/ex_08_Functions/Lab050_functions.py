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

def user_detail(name,role):
    print(f"Hi {name}! you are selected as {role}")

user_detail("Vijay","SDET")
user_detail(role="DS",name="Guru")




