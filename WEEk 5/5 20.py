str="nani babu"
char=[]
print(f"String is' {str}'")
for i in str:
    if i in char:
        continue
    else:
        char.append(i)
str=""
for i in range(len(char)):
    str+=char[i]
print(f"String after removing duplicate characters '{str}'")
"""
OUTPUT
String is' nani babu'
String after removing duplicate characters 'nai bu'
"""
