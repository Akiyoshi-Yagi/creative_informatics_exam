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


Input = list(input().split(","))
#print(Input)
shift_list = list(map(int,Input[1::2]))
blank_list = list(map(int, Input[2::2]))
max_shift = max(shift_list)
numbers= list(str(Input[0]))

def shift_mat(i,j):
    return np.full((i,j), " ")

def change_line(i):
    return np.full((i, 1),"\n")

number_arr = shift_mat(max_shift+5,1)
print(numbers)

for index, num in enumerate(numbers):
    shift_num = shift_list[index]
    if num == "0":
        number_mat = np.append(np.append(shift_mat(shift_num,4),zero,axis=0), shift_mat(max_shift-shift_num,4),axis=0)
        number_arr = np.append(number_arr, number_mat,axis=1)
    elif num == "1":
        number_mat = np.append(np.append(shift_mat(shift_num, 1), one,axis=0), shift_mat(max_shift - shift_num,1),axis=0)
        number_arr = np.append(number_arr, number_mat,axis=1)
    elif num == "2":
        number_mat = np.append(np.append(shift_mat(shift_num, 4), two,axis=0), shift_mat(max_shift - shift_num,4),axis=0)
        number_arr = np.append(number_arr, number_mat,axis=1)
    elif num == "3":
        number_mat = np.append(np.append(shift_mat(shift_num, 4), three,axis=0), shift_mat(max_shift - shift_num,4),axis=0)
        number_arr = np.append(number_arr, number_mat,axis=1)
    elif num == "5":
        number_mat = np.append(np.append(shift_mat(shift_num, 4), five,axis=0), shift_mat(max_shift - shift_num,4),axis=0)
        number_arr = np.append(number_arr, number_mat,axis=1)
    elif num == "8":
        number_mat = np.append(np.append(shift_mat(shift_num, 4), eight,axis=0), shift_mat(max_shift - shift_num,4),axis=0)
        number_arr = np.append(number_arr, number_mat,axis=1)
    if index != len(numbers)-1:
        number_arr = np.append(number_arr, shift_mat(max_shift+5,blank_list[index]),axis=1)

number_arr = np.append(number_arr, change_line(max_shift+5), axis=1)
number_arr = number_arr[:, 1:]
print(number_arr)
#number_arr = number_arr[:,1:]


with open("out1.txt", "wt") as f:
    for i in range(len(number_arr)):
        f.write("".join(list(number_arr[i])))



'''
8153,0,4,1,3,2,6,1

'''
