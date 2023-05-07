n = int(input())
F = [0] * (n + 1)
F[0] = 1
for i in range(1, n + 1):
    F[i] = F[i - 3] + F[i - 2] + F[i - 1]
print(F[-1])