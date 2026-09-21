nested_tuple = (1, 2, [3, 4, 5])
print("Original tuple:", nested_tuple)
nested_tuple[2].append(6)
nested_tuple[2][0] = 99
print("Modified tuple:", nested_tuple)

#OUTPUT
#Original tuple: (1, 2, [3, 4, 5])
#Modified tuple: (1, 2, [99, 4, 5, 6])
"""
EXPLANATION:
Tuples are immutable in the sense that the reference pointers stored inside 
them cannot be changed or reassigned after creation. 

Here, the tuple holds references to:
1. Integer object (1)
2. Integer object (2)
3. List object reference (memory address of [3, 4, 5])

We cannot replace the list object with a new object (e.g., nested_tuple[2] = [10]), 
as that would alter the tuple's internal reference and raise a TypeError. 

However, the list object itself is mutable. Modifying the contents of the list 
(via .append() or index assignment) changes the list in-place in memory without 
altering the memory address referenced by the tuple. Therefore, the tuple's 
immutability constraint remains intact.
"""


