A = []
K = int(input())
for i in range(1,K):
    if i**3 <= K: A.append(i**3)
    else: break
    
INF = 10 ** 10
F = [INF] * (K + 1)
F[0] = 0
for k in range(1, K + 1):
    for i in range(len(A)):
        if k - A[i] >= 0 and F[k - A[i]] <= F[k]:
            F[k] = F[k - A[i]]
    F[k] += 1

Ans = []
k = K
while k != 0:
    for i in range(len(A)):
        if k - A[i] >= 0 and F[k] == F[k - A[i]] + 1:
            Ans.append(A[i])
            k -= A[i]
print(len(Ans))
# for i in range(len(Ans)):
#     Ans[i] = int(Ans[i]**(1/3))
# print(Ans[::-1])