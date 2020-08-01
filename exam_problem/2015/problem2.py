with open("program.txt") as f:
    sentence = f.readlines()

sentence = [i.replace("\n", "") for i in sentence]
for index, j in enumerate(sentence):
    if "main" in j:
        print(index, j)
