# Two separate lists
keys = ["name", "age", "city", "job"]
values = ["Alex", 29, "Seattle", "Developer"]

# Creating a dictionary using zip() and dict()
person = dict(zip(keys, values))

print("Keys list:", keys)
print("Values list:", values)
print("Combined Dictionary:", person)
