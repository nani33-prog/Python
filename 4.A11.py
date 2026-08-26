LIST = [3,4,2,44,5,2,88]
print("Original list",LIST)
LIST.append(23)
print("List after append 23",LIST)
LIST.insert(4,49)
print("List after inserting 49 at 4 index",LIST)
LIST.extend([55])
print("List after extend element 55",LIST)
LIST.remove(44)
print("List after removing 44",LIST)
LIST.pop()
print("List after normal pop",LIST)
LIST.pop(6)
print("List after poping element atindex 6",LIST)
LIST.sort()
print("List after sort",LIST)
LIST.reverse()
print("Reverse of List",LIST)
print("No.of 2's in list:",LIST.count(2))
print("Element at index 4:",LIST.index(4))

#OUTPUT
#Original list [3, 4, 2, 44, 5, 2, 88]
#List after append 23 [3, 4, 2, 44, 5, 2, 88, 23]
#List after inserting 49 at 4 index [3, 4, 2, 44, 49, 5, 2, 88, 23]
#List after extend element 55 [3, 4, 2, 44, 49, 5, 2, 88, 23, 55]
#List after removing 44 [3, 4, 2, 49, 5, 2, 88, 23, 55]
#List after normal pop [3, 4, 2, 49, 5, 2, 88, 23]
#List after poping element atindex 6 [3, 4, 2, 49, 5, 2, 23]
#List after sort [2, 2, 3, 4, 5, 23, 49]
#Reverse of List [49, 23, 5, 4, 3, 2, 2]
#No.of 2's in list: 2
#Element at index 4: 3









