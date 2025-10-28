# Print even numbers between 1 and 20
# Using for loop
even=[]
for i in range(1,20+1):
    if i%2==0:
        even.append(i)
print(even)

# Without list
for k in range(1,20+1):
    if k%2==0:
        print(k,end=' ')
print()

#Using While Loop
j=1
while j<21:
    if j%2==0:
        print(j,end=' ')
    j+=1
