n=int(input("Enter n value:"))
num = 1
for i in range(n+1):
    for j in range(i):
        print(num, end=" ")
        num+=1
    print()

#OUTPUT
#Enter n value:5

#1 
#2 3 
#4 5 6 
#7 8 9 10 
#11 12 13 14 15 


