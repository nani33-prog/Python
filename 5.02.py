String="nani"
n=len(String)
#without slicing
print(f"Given String:'{String}'")
print("Reverse of sting without slicing :")
print("".join(reversed(String)))
#with slicing
reverse=String[::-1]
print(f"Reverse of String with slicing:'{reverse}'")
"""
OUTPUT
Given String:'nani'
Reverse of sting without slicing :
inan
Reverse of String with slicing:'inan'
"""


