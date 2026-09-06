List=[1,2,3,45,5,7,6,5,5,4,3,7,45,83,0,99]
print("Original List is :",List)
List=set(List)
print("Unique List(set):",List)
List=sorted(List)
print("Unique List(sorted):",List)

"""
OUTPUT
Original List is : [1, 2, 3, 45, 5, 7, 6, 5, 5, 4, 3, 7, 45, 83, 0, 99]
Unique List(set): {0, 1, 2, 3, 4, 5, 6, 7, 99, 45, 83}
Unique List(sorted): [0, 1, 2, 3, 4, 5, 6, 7, 45, 83, 99]
"""

