Sentence = "My name is Nani"
print("Sentence is\n",Sentence)
words=Sentence.split()
result=""
for i in range(len(words)-1,-1,-1):
    result+=words[i]+" "
print("Reversed sentence is\n",result)
"""
OUTPUT:
Sentence is
 My name is Nani
Reversed sentence is
 Nani is name My
"""
