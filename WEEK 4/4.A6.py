numbers = [67,43,5,2,5,44,9,2,4,88]
n=len(numbers)
print(numbers)
First3Numbers=numbers[:3]
print("First 3 numbers :",First3Numbers)
Last3Numbers=numbers[-3:]
print("Last 3 numbers :",Last3Numbers)
AlternateNumbers=numbers[::2]
print("Alternate numbers :",AlternateNumbers)

#OUTPUT
#[67, 43, 5, 2, 5, 44, 9, 2, 4, 88]
#First 3 numbers : [67, 43, 5]
#Last 3 numbers : [2, 4, 88]
#Alternate numbers : [67, 5, 5, 9, 4]
