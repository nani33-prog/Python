String="Nani Babu"
key='a'
print("String is",String)
print("Character is",key)
for i in range(len(String)):
    if String[i]==key:
        print("Index of first occurance is",i)
        break
for i in range(len(String)-1,0,-1):
    if String[i]==key:
        print("Index of last occurance is",i)
        break
"""
OUTPUT:
String is Nani Babu
Character is a
Index of first occurance is 1
Index of last occurance is 6
"""
        
