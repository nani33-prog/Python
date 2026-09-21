string1 = "Nani"
string2 = "inan"

a = string1.replace(" ", "").lower()
b = string2.replace(" ", "").lower()
if sorted(a) == sorted(b):
    print(f"{a} and {b} are Anagrams")
else:
    print(f"{a} and {b} are Not anagrams")
"""
OUTPUT:
nani and inan are Anagrams
"""
