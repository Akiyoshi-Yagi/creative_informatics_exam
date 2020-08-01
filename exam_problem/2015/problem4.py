with open("program.txt") as f:
    sentence = f.readlines()

sentence = [i.replace("\n", "") for i in sentence]


ans = []

for index, line in enumerate(sentence):
    if line not in ans:
        if line in sentence[index+1:]:
            ans.append(line)

for l in ans:
    print(l)

print(len(ans))
