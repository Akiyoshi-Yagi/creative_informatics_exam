import re

with open("prog2.txt") as f:
    stn = f.readlines()
stn_l = [x.replace("\n","") for x in stn]

cmd_l = []
v_dict = {}

def read_data(stn):
    cmd, op1, op2 = stn.split(" ")

    return (cmd, is_num(op1), is_num(op2))

def is_num(a):
    if re.match(r"-*[0-9]+", a):
        return int(a)
    else:
        return a

def exe_cmd(cmd, op1, op2):
    if cmd == "SET":
        v_dict[op1] = op2
        return
    elif cmd == "ADD":
        if type(op1) == int:
            v_dict[op2] += op1
        else:
            v_dict[op2] += v_dict[op1]
        return
    elif cmd == "PRN":
        if type(op1) != int:
            op1 = v_dict[op1]
        if type(op2) != int:
            op2 = v_dict[op2]
        print(op1, op2)


for i in stn_l:
    cmd, op1, op2 = read_data(i)
    exe_cmd(cmd, op1, op2)


