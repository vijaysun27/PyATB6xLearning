# Print right triangle using for loop
def right_triangle(x,y):
    print("Printing right triangle using for Loop")
    for i in range(x,y):
        print(i*'*')

    print()
    print("Printing right triangle using while loop")

    while x < y:
        print(x * '*')
        x += 1

right_triangle(1,6)




