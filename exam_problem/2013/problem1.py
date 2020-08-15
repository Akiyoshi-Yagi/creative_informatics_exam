import re

with open("prog1.txt") as f:
    stn = f.readlines()
stn_l = [x.replace("\n","") for x in stn]

cmd_l = []

def read_data(stn):
    cmd, op1, op2 = stn.split(" ")

    return (cmd, is_num(op1), is_num(op2))

def is_num(a):
    if re.match(r"-*[0-9]+", a):
        return int(a)
    else:
        return a

for i in stn_l:
    print(read_data(i))
