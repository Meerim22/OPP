n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
m=0
for i in range(n):
    s = sum([A[i][j] for j in range(n)])
    if s > 1:
        m += s
print(m//2)