with open("program.txt") as f:
    sentence = f.readlines()

sentence = [i.replace("\n", "") for i in sentence]

ans = []
line_a = ""
line_b = sentence[0]
for index in range(0,len(sentence)-1):
    line_a = line_b
    line_b = sentence[index+1]

    if line_a == line_b and (line_a not in ans):
        ans.append(line_a)

for line in ans:
    print(line)
