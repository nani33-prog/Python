LIST = [3,5,-32,2,-4,-5,22]
print("Original List:",LIST)
List = [0 if item<=0 else item for item in LIST]
print(List)


#OUTPUT
#Original List: [3, 5, -32, 2, -4, -5, 22]
#[3, 5, 0, 2, 0, 0, 22]
    
