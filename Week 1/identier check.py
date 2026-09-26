
import keyword
identifiers = [
    "2value",
    "value_2",
    "_hidden",
    "class",
    "my-var",
    "MyClass",
    "total$"
    ]
for identifier in identifiers:
    if identifier.isidentifier() and not keyword.iskeyword(identifier):
        print(identifier,"valid")
    else:
        print(identifier,"invalid")


##
#OUTPUT
#2value invalid //IDENTIFIER CAN NOT START WITH NUMBERS
#value_2 valid  
#_hidden valid
#class invalid  //KEYWORDS CAN NOT BE USED AS IDENTIFIERS
#my-var invalid //"-" SYMBOL IS NOT ALLOWED
#MyClass valid
#total$ invalid  //"$" IS NOT ALLOWED

