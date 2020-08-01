import numpy as np



with open("image1.txt") as f:
    char_list = f.readlines()


x = len(char_list)
for i in range(x):
    char_list[i] = char_list[i].replace("\n", "")
    char_list[i] = list(char_list[i].split(" "))

y = len(char_list[0]) / 3

print(int(x*y))

# img = np.empty((x,y))
# for i in char_list:
#     for j in range((y/3)-1):
#

