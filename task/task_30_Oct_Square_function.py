# Q - Create a function which will take a positive number from the user and perform square of the number?

def square_num(n):
    if n<0:
        return "Enter a positive number"
    else:
        return f"Square of {n} is {n*n}"

n=int(input("Enter a positive number: "))
result = square_num(n)
print(result)