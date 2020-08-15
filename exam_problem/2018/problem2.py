with open("mat1.txt") as f:
    char = f.read()

char = char.replace(".\n","")
char = char.split(",")
char = [x.split(" ") for x in char]

line = len(char)
row = len(char[0])

print(line, row)
