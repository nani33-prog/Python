LIST1=[2,3,56,3,27,66,9]
LIST2=[11,3,33,67]
print("List1:",LIST1)
print("List2:",LIST2)
for item in LIST2:
    LIST1.append(item)
LIST1.sort()
print("Merged list after sorting:",LIST1)

#OUTPUT
#List1: [2, 3, 56, 3, 27, 66, 9]
#List2: [11, 3, 33, 67]
#Merged list after sorting: [2, 3, 3, 3, 9, 11, 27, 33, 56, 66, 67]
