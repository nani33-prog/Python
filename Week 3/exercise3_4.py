a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
print("a =",a,"b =",b,"c =",c)
if a>b:
    if a>c:
        print("a is largest")
    elif c>a:
        print("c is largest")
else:
    if b>c:
        print("b is largest")

#OUTPUT
#Enter a : 4
#Enter b : 2
#Enter c : 5
#a = 4 b = 2 c = 5
#c is largest
