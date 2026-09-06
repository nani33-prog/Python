A = set((1,2,3,4))
print("Set A =",A)
B = set((3,4,5,6))
print("Set B =",B)

#union
print("Union of A and B :",A.union(B))
#intersection
print("Intersection of A and B :",A.intersection(B))
#difference
print("Difference of A and B :",A.difference(B))
#symmetric_difference
print("Symmetric Difference of A and B :",A.symmetric_difference(B))
"""
OUTPUT
Set A = {1, 2, 3, 4}
Set B = {3, 4, 5, 6}
Union of A and B : {1, 2, 3, 4, 5, 6}
Intersection of A and B : {3, 4}
Difference of A and B : {1, 2}
Symmetric Difference of A and B : {1, 2, 5, 6}
"""
