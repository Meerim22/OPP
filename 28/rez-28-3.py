n = int(input())
A = list(map(int, input().split()))
def gis(A, n):
    INF = 10 ** 6
    F = [-INF] + [INF] * (n+1)
    for i in range(n):
        left = 0
        right = n+1
        while left+1 < right:
            middle = (left + right) // 2
            if F[middle] < A[i]: left = middle
            else: right = middle
        F[right] = A[i]
    i = n+1
    while F[i] == INF:
        i -= 1
    return i
print(gis(A,n))