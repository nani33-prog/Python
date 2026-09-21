sentence = "My name is Nani babu Velagada"
print("Original sentence is\n",sentence)
words=sentence.split()
result=""
for i in range(len(words)):
    result+=words[i].title()+" "
print("Sentence with Capitalizing the first letter of every word is\n",result)
"""
OUTPUT:
Original sentence is
 My name is Nani babu Velagada
Sentence with Capitalizing the first letter of every word is
 My Name Is Nani Babu Velagada
"""
