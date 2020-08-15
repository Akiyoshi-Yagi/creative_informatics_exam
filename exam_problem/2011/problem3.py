from collections import defaultdict

with open("s1.txt") as f:
    txt = f.read()

txt = txt.rstrip("\n")

def create_dict(txt):
    d = defaultdict(list)
    txt_list = list(txt)
    for index in range(len(txt_list)-5):
        chars = "".join(txt_list[index:index+6])
        if chars in list(d):
            pass
        else:
            d[chars] = "".join(list("00" + str(index))[-3:])
    return dict(d)

print(create_dict(txt))

