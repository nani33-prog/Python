# Two separate lists
keys = ["name", "age", "city", "job"]
values = ["Alex", 29, "Seattle", "Developer"]

# Creating a dictionary using zip() and dict()
person = dict(zip(keys, values))

print("Keys list:", keys)
print("Values list:", values)
print("Combined Dictionary:", person)


#OUTPUT
#Keys list: ['name', 'age', 'city', 'job']
#Values list: ['Alex', 29, 'Seattle', 'Developer']
#Combined Dictionary: {'name': 'Alex', 'age': 29, 'city': 'Seattle', 'job': 'Developer'}
