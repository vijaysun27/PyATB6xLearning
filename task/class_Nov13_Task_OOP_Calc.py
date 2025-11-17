'''You need to create a calculator function, but the calculator function
has to take the value from the parameterized constructor. So while creating the object,
you will pass the parameters and that will basically
return the sum of the two numbers, multiplication of two numbers. '''

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self,a,b):
        return f"Sum of {self.a} and {self.b} is {self.a+self.b}"

    def multiply(self,a,b):
        return f"Product of {self.a} and {self.b} is {self.a*self.b}"

a = float(input("Enter a: "))
b = float(input("Enter b: "))
sum = Calculator(a,b)
product = Calculator(a,b)

addition,multiplication = sum.add(a,b),product.multiply(a,b)
print(addition)
print(multiplication)

