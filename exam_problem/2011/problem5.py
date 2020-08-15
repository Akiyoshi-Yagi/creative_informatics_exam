import re
import copy

with open("c1.txt") as f:
    txt = f.read()

txt = txt.rstrip("\n")

def find_num_arr(txt):
    return re.finditer(r"[0-9]{3}", txt)

loc = []
for i in list(find_num_arr(txt)):
    loc.append(i.span()[0])

#取得した文字列をリスト化
t_list = list(txt)
original = copy.deepcopy(t_list)

diff = 0
for i in loc:
    n = "".join(t_list[i:i+3])
    if n == "000":
        num = 0
    else:
        num = int(n.lstrip("0"))
    original = original[:i+diff] + original[num:num+6] + original[i+3+diff:]
    diff += 3


print("".join(original))



