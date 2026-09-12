string="I am studying in GMRITDU"
print("String is",string)
print("After replacing 'a' with '''")
for i in string:
    if i=="a":
        i="'"
    print(i, end="")

#OUTPUT
"""
String is I am studying in GMRITDU
After replacing 'a' with '''
I 'm studying in GMRITDU
"""
