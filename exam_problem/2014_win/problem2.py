
import time


def calc_f(x):
    memo = [0] * (x+1)

    def f(x):
        if x <= 2:
            memo[x] = 1
        else:
            memo[x] = memo[x-1] + memo[x-2]

    for i in range(1,x+1):
        f(i)
    return memo[x]


start = time.time()
print(calc_f(140))
end = time.time()

print(end - start)
