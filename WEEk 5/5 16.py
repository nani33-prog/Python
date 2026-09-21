Sentence="My name is Nani Babu Velagada"
word=[]
dummy=0
print("Sentence is",Sentence)
for i in range(len(Sentence)):
    if Sentence[i]==' ':
            word.append(Sentence[dummy:i])
            dummy=i+1
word.append(Sentence[dummy:])
print("Words in Sentence are",word)
n=0
for item in word:
    if len(item)>n:
        n=len(item)
        lword=item
print("Longest Word in sentence is",lword)
"""
OUTPUT:
Sentence is My name is Nani Babu Velagada
Words in Sentence are ['My', 'name', 'is', 'Nani', 'Babu', 'Velagada']
Longest Word in sentence is Velagada
"""
