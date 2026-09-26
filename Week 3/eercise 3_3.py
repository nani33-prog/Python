a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
if((a+b)>c) and ((b+c)>a) and ((c+a)>b):
    if a==b and a==c:
        print("Equilateral Triangle")
    elif a==b or a==c or b==c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("not a valid Triangle")
    


#OUTPUT
#Enter side a: 3
#Enter side b: 3
#Enter side c: 3
#Equilateral Triangle
