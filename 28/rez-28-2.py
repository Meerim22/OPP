n = int(input())
A = list(map(int, input().split()))
def gis(A, n):
    F = [0] * n
    Prev = [-1] * n
    for i in range(n):
        for j in range(i):
            if A[j] < A[i] and F[j] > F[i]:
                F[i] = F[j]
                Prev[i] = j
        F[i] += 1
    ans = []
    i = F.index(max(F))
    ans.append(A[i])
    while Prev[i] != -1:
        i = Prev[i]
        ans.append(A[i])
    return ans[::-1]
print(gis(A,n))