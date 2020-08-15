#問題４と問題５が正しいかどうかを確かめる。

from problem4 import tran_char_to_num
from problem5 import tran_num_to_char

for i in range(1,4000):
    character = tran_num_to_char(i)
    num = tran_char_to_num(character)
    print(num, character)
    if i != num:
        print(i)
print("end")
