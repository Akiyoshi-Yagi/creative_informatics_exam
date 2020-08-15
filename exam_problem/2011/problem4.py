from collections import defaultdict

with open("s1.txt") as f:
    txt = f.read()

txt = txt.rstrip("\n")

def create_dict(txt):
    d = defaultdict(list)
    txt_list = list(txt)
    for index in range(len(txt_list)-5):
        chars = "".join(txt_list[index:index+6])
        if chars in list(d):
            pass
        else:
            d[chars] = "".join(list("00" + str(index))[-3:])
    return dict(d)

def trans_string(txt):
    d = create_dict(txt)
    txt_list = list(txt)
    l = len(txt_list)
    counter = {}
    for s in d:
        counter[s] = 0
    string = ""
    index = 0
    while index <= l-6:
        print(index)
        chars = "".join(txt_list[index:index+6])
        if chars in d:
            print(chars)
            if counter[chars] > 0:
                string += d[chars]
                index += 6
            else:
                string += txt_list[index]
                index += 1
            counter[chars] += 1
        else:
            string += txt_list[index]
            index += 1


    return string


print(trans_string(txt))

