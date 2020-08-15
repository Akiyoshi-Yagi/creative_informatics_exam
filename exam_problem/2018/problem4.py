import numpy as np
from collections import deque

m, n, s = map(int, input().split())
#cacheをキューで管理
cache = deque([],s)

ans = 0
i = 0
while i  < m:
    j = 0
    while j < m:
        d = 0
        k = 0
        while k < n:
            if [0, i, k] not in cache:
                ans += 1
            else:
                cache.remove([0, i, k])
            cache.append([0, i, k])
            if [1, k, j] not in cache:
                ans += 1
            else:
                cache.remove([1, k, j])
            cache.append([1, k, j])
            k = k + 1
        j = j + 1
    i = i + 1

print(ans)
