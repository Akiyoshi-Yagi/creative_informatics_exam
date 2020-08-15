with open("text1.txt") as f:
    l = f.read()
l = l.rstrip("\n")

char = []
for i in l.split("+"):
    for j in i.split("&"):
        j = j.lstrip("!")
        char.append(j)

char = sorted(list(set(char)))

bit_l = []
for bit in range(2**len(char)):
    for i in l.split("+"):
        is_true = True
        for j in i.split("&"):
            if "!" in j:
                j = j.lstrip("!")
                if ~(bit >> (len(char)-char.index(j)-1)) & 1:
                    pass
                else:
                    is_true = False
            else:
                if (bit >> (len(char)-char.index(j)-1)) & 1:
                    pass
                else:
                    is_true = False
        if is_true:
            bit_l.append(bit)
            break

if not bit_l:
    print("none")
else:
    ans = []
    for cmb in bit_l:
        dc = {}
        for c in char:
            if (cmb >> len(char)-char.index(c)-1) & 1:
                dc[c] = "True"
            else:
                dc[c] = "False"
        ans.append(dc)
    for _ in ans:
        print(_)




