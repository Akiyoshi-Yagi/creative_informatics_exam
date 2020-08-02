n = int(input())

ans = 0
for i in range(1,n+1):
    divisor = 0
    for j in range(1,i+1,2):
        if i % j == 0:
            divisor += 1
    if divisor == 8:
        ans += 1

print(ans)
