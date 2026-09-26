n = int(input("Enter the number: "))
i=1
if n<1:
    print("enter a positive number")
else:
    print("Multiplication table of",n)
    for i in range(1,11,1):
        print (n*i)


#OUTPUT
#Enter the number: 6
#Multiplication table of 6
#6
#12
#18
#24
#30
#36
#42
#48
#54
#60
