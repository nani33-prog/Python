String="Nani Babu"
n=len(String)
print("Given string:",String)
print("String after reversing case vice verse:")
for i in String:
    if i.isalpha()==True:
        if i==i.lower():
            j=i.upper()
        else:
            j=i.lower()
        print(j,end="")
    else:
        print(i,end="")
#OUTPUT
#Given string: Nani Babu
#String after reversing case vice verse:
#nANI bABU
