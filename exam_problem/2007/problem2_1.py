from collections import Counter

with open("q21.txt") as f:
    sentence = f.read()

letters = list(sentence)

L = []
for letter in letters:
    if 65<=ord(letter)<=90 or 97<=ord(letter)<=122:
        L.append(letter.lower())
    else:
        pass
counter = Counter(L)
print(counter)
