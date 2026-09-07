String=input("Enter a string:")
String=String.lower()
vowels=consonents=digits=spaces=0
for char in String:
    if char.isalpha():
        if char in {'a','e','i','o','u'}:
            vowels+=1
        else:
            consonents+=1
    elif char.isdigit:
        if char==" ":
            spaces+=1
        else:
            digits+=1
print("No.of Vowels =",vowels)
print("No.of Consonentss =",consonents)
print("No.of Digits =",digits)
print("No.of Spaces =",spaces)
"""
OUTPUT
Enter a string:Nani Babu 33
No.of Vowels = 4
No.of Consonentss = 4
No.of Digits = 2
No.of Spaces = 2
"""
