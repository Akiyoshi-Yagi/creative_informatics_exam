num = list(input())

ans = 0
t = 1
for i in reversed(num):
    ans += int(i)*t
    t *= 4

print(ans)



