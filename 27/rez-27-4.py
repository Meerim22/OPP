A = str(input())
B = str(input())
n = len(A)
m = len(B)
F = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            F[i][j] = F[i - 1][j - 1]
        else:
            F[i][j] = min(F[i - 1][j-1], F[i-1][j], F[i][j-1])+1
            if i>=2 and j>=2 and A[i-2:i] == B[j - 2:j][::-1]:
                F[i][j] = min(F[i][j], F[i-2][j-2]+1)
            # F[i][j] = min(F[i-2][j-2], F[i - 1][j-1], F[i-1][j], F[i][j-1])+1
print(F[n][m])
# for i in F:
#     print(i)