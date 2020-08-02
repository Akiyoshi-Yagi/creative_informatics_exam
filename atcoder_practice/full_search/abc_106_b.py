n = int(input())

odd_prime = [3,5,7,11,13]
ans = 0
#2*2*2=8
for i in range(3):
    for j in range(i+1,4):
        for h in range (j+1,5):
            if odd_prime[i] * odd_prime[j] * odd_prime[h] <= n:
                ans += 1
#4*2=8
for i in range(1,5):
    if 3**3 * odd_prime[i] <= n:
        ans += 1

print(ans)
