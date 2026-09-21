Sentence="My name is Nani Babu"
key=' '
n=1
print(f"Sentence is'{Sentence}'")
for i in range(len(Sentence)):
    if Sentence[i]==key:
        n+=1
print("Number of words in Sentence are",n)

"""
OUTPUT:
Sentence is'My name is Nani Babu'
Number of words in Sentence are 5
"""
