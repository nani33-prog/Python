Items = {"Dosa": 35, "Idli": 20, "Upma": 25, "Poori": 30}

# Initialize variables using max() and min() with key=Items.get
highest_item = max(Items, key=Items.get)
lowest_item = min(Items, key=Items.get)

print(f"Item with Highest Price is {highest_item} (Price: {Items[highest_item]})")
print(f"Item with Lowest Price is {lowest_item} (Price: {Items[lowest_item]})")


"""
OUTPUT
Item with Highest Price is Dosa (Price: 35)
Item with Lowest Price is Idli (Price: 20)
"""
