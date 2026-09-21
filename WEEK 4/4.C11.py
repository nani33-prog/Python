String=input("Enter a string:")
char_counts = {}

for char in String:
    char_counts[char] = char_counts.get(char, 0) + 1

print("Original String:", String)
print("Character Frequencies:", char_counts)

"""
OUTPUT
Enter a string:NANI BABU==33
Original String: NANI BABU==33
Character Frequencies: {'N': 2, 'A': 2, 'I': 1, ' ': 1, 'B': 2, 'U': 1, '=': 2, '3': 2}
"""
