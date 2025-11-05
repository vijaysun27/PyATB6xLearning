# Print right triangle using for loop
def right_triangle(y):
    print("Printing right triangle using for Loop")
    if y<=0:
        print("Number of lines must be greater than zero")
    else:
        for i in range(1,y+1):
            print(i*'*')

        print()
        print("Printing right triangle using while loop")

        x=1
        while x <= y:
            print(x * '*')
            x += 1

right_triangle(5)




