import re
from collections import deque

with open("prog4.txt") as f:
    stn = f.readlines()
stn_l = [x.replace("\n","") for x in stn]

cmd_l = []
v_dict = {}
loc = deque([])

def read_data(stn):
    cmd, op1, op2 = stn.split(" ")
    return (cmd, is_num(op1), is_num(op2))

def is_num(a):
    if re.match(r"-*[0-9]+", a):
        return int(a)
    else:
        return a

def exe_cmd(cmd, op1, op2, n):
    if cmd == "SET":
        v_dict[op1] = op2
        return 1

    elif cmd == "ADD":
        if type(op1) == int:
            v_dict[op2] += op1
        else:
            v_dict[op2] += v_dict[op1]
        return 1

    elif cmd == "PRN":
        if type(op1) != int:
            op1 = v_dict[op1]
        if type(op2) != int:
            op2 = v_dict[op2]
        print(op1, op2)
        return 1

    elif cmd == "CMP":
        if type(op1) != int:
            op1 = v_dict[op1]
        if type(op2) != int:
            op2 = v_dict[op2]
        if op1 == op2:
            return 2
        else:
            return 1

    elif cmd == "JMP":
        return op1

    elif cmd == "SUB":
        loc.append(n)
        return op1

    elif cmd == "BAK":
        return loc.pop() - n +1


for sen in stn_l:
    cmd_l.append(read_data(sen))

n = 0
while n  < len(cmd_l):
    cmd, op1, op2 = cmd_l[n]
    print(cmd, op1, op2, n)
    res = exe_cmd(cmd, op1, op2, n)
    n += res



