import copy

n, q = map(int, input().split())
x_sum = [0] * (n+1)
adj_list = [[] for _ in range(n+1)]

counter = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    adj_list[a].append(b)

for _ in range(q):
    p, x = map(int, input().split())
    x_sum[p] += x

stack = [1]
counter[1] = x_sum[1]
while stack:
    parent = stack.pop()
    children = adj_list[parent]
    if children:
        for child in children:
            counter[child] = x_sum[child] + counter[parent]
            stack.append(child)

counter = [str(x) for x in counter]
print(" ".join(counter[1:]))
