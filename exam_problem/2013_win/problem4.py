import copy
with open("text1.txt") as f:
    ol = f.read()
ol = ol.strip("\n")

alp = ["a","b","c","d","e","f","g"]

chr = []
for i in list(ol):
    if i in alp:
        chr.append(i)

chr = sorted(list(set(chr)))
print(chr)
bit_l = []
for i in range(2**len(chr)):
    l = copy.deepcopy(ol)
    for c in chr:
        nc = (i >> (len(chr)-chr.index(c)-1)) & 1
        l = l.replace(c,str(nc))
    l = l.replace("!"," not ").replace("&", " and ").replace("+"," or ")
    print(l)
    if eval(l):
        bit_l.append(i)
print(bit_l)

if not bit_l:
    print("none")
else:
    ans = []
    for cmb in bit_l:
        dc = {}
        for c in chr:
            if (cmb >> len(chr)-chr.index(c)-1) & 1:
                dc[c] = "True"
            else:
                dc[c] = "False"
        ans.append(dc)
    for _ in ans:
        print(_)

