Set=set((11,22,33,44,55))
print("Given set:",Set)
Set.add(66)
print("Set after adding 66 with '.add()\n",Set)
Set.update((88,99))
print("Set after adding 88,99 with '.update()\n",Set)
"""
OUTPUT
Given set: {33, 11, 44, 22, 55}
Set after adding 66 with '.add()
 {33, 66, 11, 44, 22, 55}
Set after adding 88,99 with '.update()
 {33, 66, 99, 11, 44, 22, 55, 88}
 """
