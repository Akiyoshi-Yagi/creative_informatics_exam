with open("text1.txt") as f:
    l = f.read()
l = l.rstrip("\n")
a = []
for i in l.split("+"):
    print(i)
