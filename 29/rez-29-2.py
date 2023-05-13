n = int(input())
A = list(map(int, input().split()))
K = int(input())
INF = 10 ** 10
F = [INF] * (K + 1)
F[0] = 0
for k in range(1, K + 1):
    for i in range(len(A)):
        if k - A[i] >= 0 and F[k - A[i]] < F[k]:
            F[k] = F[k - A[i]]
    F[k] += 1
if F[-1] != 1:
    print('No solution')
else:
    Ans = []
    k = K
    while k != 0:
        for i in range(len(A)):
            if k - A[i] >= 0 and F[k] == F[k - A[i]] + 1:
                Ans.append(A[i])
                k -= A[i]
    print(*Ans)