n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
F = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            F[i][j] = F[i - 1][j - 1] + 1
        else:
            F[i][j] = max(F[i - 1][j], F[i][j - 1])
Ans = []
i = n
j = m
while i > 0 and j > 0:
    if A[i - 1] == B[j - 1]:
        Ans.append(A[i - 1])
        i -= 1
        j -= 1
    elif F[i - 1][j] == F[i][j]: i -= 1
    else: j -= 1
Ans = Ans[::-1]
print(*Ans)