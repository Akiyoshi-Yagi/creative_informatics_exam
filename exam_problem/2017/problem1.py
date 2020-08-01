import numpy as np
import pandas as pd

#めんどくさかったので012358だけ実装した

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
interval = np.array([["  "],
                     ["  "],
                     ["  "],
                     ["  "],
                     ["  "]])
change_line = np.array([["\n"],
                        ["\n"],
                        ["\n"],
                        ["\n"],
                        ["\n"],
                        ])

numbers = list(str(input()))
print(numbers)
number_arr = interval
for i in numbers:
    if i == "0":
        number_arr = np.concatenate([number_arr, zero],axis=1)
    elif i == "1":
        number_arr = np.concatenate([number_arr, one],axis=1)
    elif i == "2":
        number_arr = np.concatenate([number_arr, two], axis=1)
    elif i == "3":
        number_arr = np.concatenate([number_arr, three], axis=1)
    elif i == "5":
        number_arr = np.concatenate([number_arr, five], axis=1)
    elif i == "8":
        number_arr = np.concatenate([number_arr, eight], axis=1)
    number_arr = np.concatenate([number_arr, interval],1)
number_arr = number_arr[:,1:-1]
number_arr = np.concatenate([number_arr, change_line],1)

with open("out1.txt", "wt") as f:
    for i in range(len(number_arr)):
        f.write("".join(list(number_arr[i])))



