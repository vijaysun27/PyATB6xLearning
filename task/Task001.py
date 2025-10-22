#area of cirlce
import math
r = float(input("Enter radius: "))
area_of_circle = 3.14*(r**2)

print(f"The area of circle is {area_of_circle}")
print()

area_of_circle_2 = 3.14*pow(r,2)
print(f"The area of circle is {area_of_circle_2:.2f}")

area_of_circle_3 = math.pi*pow(r,2)
print(f"The area of circle is {area_of_circle_3:.3f}")