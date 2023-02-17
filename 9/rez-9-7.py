n, k = map(int, input().split())
t = [0 for _ in range(n + 1)]
for _ in range(k):
    m, p, s = map(int, input().split())
    t[m] -= s
    t[p] += s
print(*t[1:])