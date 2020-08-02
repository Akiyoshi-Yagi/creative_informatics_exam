import bisect as bs

n = int(input())

a_l = list(map(int, input().split()))
b_l = list(map(int, input().split()))
c_l = list(map(int, input().split()))

a_l.sort()
b_l.sort()
c_l.sort()

ans = 0
for b in b_l:
    ans += bs.bisect_left(a_l,b) * (n-bs.bisect_right(c_l,b))
print(ans)


'''
以下の方法だと、N*logN*logN
for i in range(n):
    index_1 = bs.bisect_right(b_l,a_l[i])
    for j in range(index_1,n):
        index_2 = bs.bisect_right(c_l,b_l[j])
        ans += (n-index_2)
print(ans)
'''
