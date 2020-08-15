import re

with open("c1.txt") as f:
    txt = f.read()

def find_num_arr(txt):
    return re.findall(r"[0-9]{3}", txt)

print(len(find_num_arr(txt)))
