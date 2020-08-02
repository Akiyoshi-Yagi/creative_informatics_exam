n, m = map(int,input().split())

k = []
s_l = []
for _ in range(m):
    l = list(map(int, input().split()))
    k.append(l[0])
    s_l.append(l[1:])

p = list(map(int,input().split()))

ans = 0
for i in range(2**n):
    valid = 1
    for j in range(m):
        on = 0
        for s in s_l[j]:
            on += (i >> (s-1) & 1)
        if on % 2 == p[j]:
            valid *= 1
        else:
            valid *= 0
    ans += valid

print(ans)



