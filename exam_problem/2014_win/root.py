def root(k):
    x = k
    e = 10**-8
    error = float("inf")
    def f_k(x):
        return x**2 - k
    def f_diff_k(x):
        return 2*x

    while error > e:
        x = x - (f_k(x)/f_diff_k(x))
        error = f_k(x) - 0
    return x

print(root(5))


