with open("program.txt") as f:
    sentence = f.readlines()

sentence = [list(i.replace("\n", "")) for i in sentence]

ans = 0
for j in sentence:
    for h in j:
        if h == ";":
            ans += 1

print(ans)
