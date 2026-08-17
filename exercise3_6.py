c = input("Enter a character : ")
if c.isalpha():
    c_lower = c.lower()
    if c_lower in {'a','e','i','o','u'}:
        print(c,"is vowel")
    else:
        print(c,"is consonant")

elif c.isdigit():
    print(c,"is a digit")

else :
    print(c,"is a special character")

#OUTPUT
#Enter a character : r
#r is contant
