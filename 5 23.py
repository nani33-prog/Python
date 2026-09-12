str='nani'
print(f"String is '{str}'")
list=[]
for i in str:
    list.append(i)
print(f"list of characters in string '{list}'")
str=""
for i in range(len(list)):
    str+=list[i]
print(f"string after converting back to string '{str}'")
"""
OUTPUT:
String is 'nani'
list of characters in string '['n', 'a', 'n', 'i']'
string after converting back to string 'nani'
"""
