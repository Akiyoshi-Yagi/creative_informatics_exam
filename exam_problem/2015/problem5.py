with open("program.txt") as f:
    sentence = f.readlines()

sentence = [i.replace("\n", "") for i in sentence]
print(sentence)

def compare(x, y):
    if len(x) > len(y):
        y = y + " " * (len(x)-len(y))
    elif len(x) < len(y):
        x = x + " " * (len(y) - len(x))
    else:
        pass

    not_same = 0
    for i in range(len(x)):
        if not_same >= 5:
            break
        else:
            if x[i] != y[i]:
                not_same += 1
            else:
                pass

    if 0 < not_same < 5:
        return True
    else:
        return False

ans = []
for index, line_a in enumerate(sentence):
    if index == len(sentence):
        continue
    for line_b in sentence[index+1:]:
        if compare(line_a, line_b):
            if ([line_a, line_b] not in ans) and ([line_b, line_a] not in ans):
                ans.append([line_a, line_b])
            else:
                pass
        else:
            pass

for a in ans:
    print(a[0]+" ~ "+a[1])





