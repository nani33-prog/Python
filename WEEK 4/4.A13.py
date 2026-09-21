LIST=[4,3,2,55,3,55,7,4,3,3,333,0]
max=sum=min=0
n=len(LIST)
for i in range(n):
    if LIST[i]>max:
        max=LIST[i]
    if LIST[i]<min:
        min=LIST[i]
    sum+=LIST[i]
print(LIST)
print(f"Maximum number is {max},Minimum number is {min},Sum of all is {sum}")

#OUTPUT
#[4, 3, 2, 55, 3, 55, 7, 4, 3, 3, 333, 0]
#Maximum number is 333,Minimum number is 0,Sum of all is 472
