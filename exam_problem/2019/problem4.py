import numpy as np

def select_k(k):


    with open("image1.txt") as f:
        char_list = f.readlines()
    x = len(char_list)
    for i in range(x):
        char_list[i] = char_list[i].replace("\n", "")
        char_list[i] = list(map(int,list(char_list[i].split(" "))))
        y = len(char_list[i]) / 3
        char_list[i] = [char_list[i][i:i+3] for j in range(0,len(char_list[i]),3)]
        for h in char_list[i]:
            h.append((h[0])**2+(h[1])**2+(h[2])**2)
    one_d_list = []
    for s in char_list:
        for t in s:
            one_d_list.append(t)


    for index, l in enumerate(one_d_list):
        l.append(index)
    sorted_flatten = sorted(one_d_list, key=lambda x:x[3])

    print(sorted_flatten[int(len(one_d_list)/2)])


# img = np.empty((x,y))
# for i in char_list:
#     for j in range((y/3)-1):
#

