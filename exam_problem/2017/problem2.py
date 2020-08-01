import numpy as np

zero = np.array([["*","*","*","*"],
                 ["|"," "," ","|"],
                 ["*"," "," ","*"],
                 ["|"," "," ","|"],
                 ["*","*","*","*"]])
one = np.array([["*"],
                ["|"],
                ["*"],
                ["|"],
                ["*"]])
two = np.array([["*","*","*","*"],
                [" "," "," ","|"],
                ["*","*","*","*"],
                ["|"," "," "," "],
                ["*","*","*","*"]])
three = np.array([["*","*","*","*"],
                  [" "," "," ","|"],
                  ["*","*","*","*"],
                  [" "," "," ","|"],
                  ["*","*","*","*"]])
five = np.array([["*","*","*","*"],
                 ["|"," "," "," "],
                 ["*","*","*","*"],
                 [" "," "," ","|"],
                 ["*","*","*","*"]])
eight = np.array([["*","*","*","*"],
                 ["|"," "," ","|"],
                 ["*","*","*","*"],
                 ["|"," "," ","|"],
                 ["*","*","*","*"]])
with open("out1.txt") as f:
    line_list = f.readlines()

#print(line_list)
num_4_list = [zero, two, three, five, eight]

num_arr = 0
for index, line in enumerate(line_list):
    if index == 0:
        num_arr = np.array([list(line)])
        continue
    num_arr = np.append(num_arr, np.array([list(line)]), axis=0)

num_arr = num_arr[:, :-1]
ans = []
while (num_arr.shape[1] != 0):
    if num_arr.shape[1] >= 4:
        if any( (num_arr[:, :4] == x).all() for x in num_4_list):
            if (num_arr[:, :4] == zero).all():
                ans.append(0)
            elif (num_arr[:, :4] == two).all():
                ans.append(2)
            elif (num_arr[:, :4] == three).all():
                ans.append(3)
            elif (num_arr[:, :4] == five).all():
                ans.append(5)
            elif (num_arr[:, :4] == eight).all():
                ans.append(8)
            num_arr = num_arr[:, 4:]
        else:
            ans.append(1)
            num_arr = num_arr[:, 1:]
        if num_arr.shape[1] != 0:
            num_arr = num_arr[:, 2:]
            continue
    else:
        ans.append(1)
        num_arr = num_arr[:, 1:]
    if num_arr.shape[1] != 0:
        num_arr = num_arr[:, 2:]

print(ans)





