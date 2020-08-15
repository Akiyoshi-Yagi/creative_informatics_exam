with open("q1.txt") as f:
    s = f.read()

words = s.replace("\n"," ").split(" ")[:-1]

def decode(c,i):
    n = ord(c)
    if 65<= n <= 90:
        n = ord(c) - i
        if n <= 64:
            n += 26
        return chr(n)
    elif 97 <= n <= 122:
        n = ord(c) - i
        if n <= 96:
            n += 26
        return chr(n)
    else:
        return c


for i in range(1,26):
    f_list = []
    for word in words:
        o = ""
        for char in word:
            o += (decode(char, i))
        f_list.append(o)
    print("---------")
    print(i)
    print(" ".join(f_list))

