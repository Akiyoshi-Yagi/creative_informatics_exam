
def translate(char):
    if char == "a":
        return 0
    elif char == "b":
        return 1
    elif char == "c":
        return 2
    elif char == "d":
        return 3
    elif char == "e":
        return 4
    elif char == "f":
        return 5
    elif char == "g":
        return 6
    elif char == "h":
        return 7

string = list(input())

ans = 0
s = 1
for i in reversed(string):
    num = translate(i)
    ans += num*s
    s *= 8

print(ans)
