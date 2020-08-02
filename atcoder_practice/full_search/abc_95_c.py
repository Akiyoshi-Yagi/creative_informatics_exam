a, b, c, x, y = map(int, input().split())

p = []
for i in range(0,100001):
    p.append(i * 2 * c + max(0,x-i) * a + max(0,y-i) * b)

print(min(p))
