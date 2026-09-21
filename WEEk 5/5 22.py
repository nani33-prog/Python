str=input("Enter a string:")
char=[]
dup=[]
n=0
for i in str:
    if i in char:
        if i in dup:
            n+=1
        else:
            dup.append(i)
            n+=1

    else:
        char.append(i)
print("duplicate characters are",dup)
print("Number os duplicate characters is",n)
"""
OUTPUT:
Enter a string:aaaabbbbaacc
duplicate characters are ['a', 'b', 'c']
Number os duplicate characters is 9
"""
