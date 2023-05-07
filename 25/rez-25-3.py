n, k = map(int, input().split())
F = [0] * (n + 1)
F[0] = 1
for i in range(1, n + 1):
    m = 0
    for l in range(1,k+1):
        m += F[i - l]
    F[i] = m
print(F[-1])