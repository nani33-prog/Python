def my_find(text, sub):
    if sub == "":
        return 0
    for i in range(len(text) - len(sub) + 1):
        matched = True
        for j in range(len(sub)):
            if text[i + j] != sub[j]:
                matched = False
                break
        if matched:
            return i
    return -1
def my_count(text, sub):
    if sub == "":
        return len(text) + 1
    count = 0
    for i in range(len(text) - len(sub) + 1):
        matched = True
        for j in range(len(sub)):
            if text[i + j] != sub[j]:
                matched = False
                break
        if matched:
            count += 1
    return count
sentence = "naninani"
sub="ni"
print(my_find(sentence, sub))   
print(my_count(sentence, sub))
"""
OUTPUT:
2
2
"""


