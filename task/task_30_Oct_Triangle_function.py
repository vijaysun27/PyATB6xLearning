#Q - Create a function which will take the 3 values from the user,
# which are length of the triangle.  side1, side2, side2
# i/p - int side1 == side2 =side3 → isoceles
# o/p = result in string - iso, eq, scalene

def find_triangle(side1,side2,side3):
    if side1==side2==side3:
            print("This is an Equilateral Triangle")
    elif side1==side2 or side2==side3 or side3==side1:
            print("This is an Isosceles Triangle")
    else:
        print("This is a Scalene Triangle")

side1 = float(input("Enter side_1: "))
side2 = float(input("Enter side_2: "))
side3 = float(input("Enter side_3: "))
find_triangle(side1,side2,side3)


