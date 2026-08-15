n = int(input("Enter a number: "))
sum=0
if n==0:
    print("Sum is 0 and Average is 0")
else:
    while n!=0:
        digit=n%10
        n=n//10
        sum+=digit

    print("Sum is",sum)
    print("Average is",sum/3)

#OUTPUT
#Enter a number: 345
#Sum is 12
#Average is 4.0
