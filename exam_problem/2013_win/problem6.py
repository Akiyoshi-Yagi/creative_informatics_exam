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

bit_l = []
for i in range(2**len(chr)):
    l = copy.deepcopy(ol)
    for c in chr:
        nc = (i >> (len(chr)-chr.index(c)-1)) & 1
        l = l.replace(c,str(nc))
    l = l.replace("!"," not ").replace("&", " and ").replace("+"," or ")
    if  not eval(l):
        bit_l.append(i)

if not bit_l:
    print("none")
else:
    pl = []
    for cmb in bit_l:
        dc = {}
        for c in chr:
            if (cmb >> len(chr)-chr.index(c)-1) & 1:
                dc[c] = "True"
            else:
                dc[c] = "False"
        pl.append(dc)
    ans = []
    for l in pl:
        string = []
        for k in l:
            if l[k] == "False":
                string.append(k)
            else:
                string.append("!"+k)
        st = "+".join(string)
        ans.append("("+st+")")
    ans = "&".join(ans)
    print(ans)



