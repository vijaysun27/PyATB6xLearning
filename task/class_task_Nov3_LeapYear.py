def find_leap_year(year):

    if year%400==0:
        return f"{year} is a leap year"
    elif year%100!=0 and year%4==0:
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"

y = int(input("Enter a valid year: "))
result = find_leap_year(y)
print(result)
