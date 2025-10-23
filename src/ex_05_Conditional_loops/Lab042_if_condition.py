mark = int(input("Enter mark: "))

if mark >100 or mark<=-1:
    print("Enter valid mark")
else:
    if mark>=90 and mark<=100:
        print("Your grade is A")
    elif mark>=80 and mark<=89:
        print("Your grade is B")
    elif mark>=70 and mark<=79:
        print("Your grade is C")
    elif mark>=60 and mark<=69:
        print("Your grade is D")
    elif mark>=50 and mark<=59:
        print("Your grade is F")
    else:
        print("Your grade is G")

