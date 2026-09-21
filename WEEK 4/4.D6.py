Set=set([33,4,22,5,7])
print(Set)
#remove()
Set.remove(5)
print("Set after removig existing element 5:",Set)
#discard
Set.discard(77)
print("Set after removig non existing element 77:",Set)
Set.discard(7)
print("Set after removig existing element 7:",Set)

"""
OUTPUT
{33, 4, 5, 7, 22}
Set after removig existing element 5: {33, 4, 7, 22}
Set after removig non existing element 77: {33, 4, 7, 22}
Set after removig existing element 7: {33, 4, 22}

EXPLAINATION
set.remove() raises error while removing non existing item but not in discard()
"""
