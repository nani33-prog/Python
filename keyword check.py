INPUT = input("Enter a Word : ")
import keyword
if keyword.iskeyword(INPUT):
    print(INPUT," is a PYTHON keyword")
else:
    print(INPUT," is not a PYTHON keyword")

#OUTPUT
#Enter a Word : input
#input  is not a PYTHON keyword

#Enter a Word : False
#False  is a PYTHON keyword
