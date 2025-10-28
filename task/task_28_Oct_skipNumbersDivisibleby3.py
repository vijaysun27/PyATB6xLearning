# Skip numbers divisible by 3, from (0,100)
# Using for loop
for i in range(0,101):
    if i%3==0:
        continue
    print(i,end=' ')

print()
#Using While loop

j=0
while j<101:
    if j%3==0:
        j+=1
        continue
    print(j,end=' ')
    j+=1