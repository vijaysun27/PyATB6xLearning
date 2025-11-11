numbers = [1,2,3,4,5,6]

def sq(x):
    return x**2

square_numbers = list(map(sq,numbers))
print(square_numbers)