n, m = map(int, input().split())
arr = [[0 for j in range(m+1)] for i in range(n+1)]
arr[1][1] = 1
for i in range(2, n + 1):
    for j in range(2, m + 1):
        arr[i][j] = arr[i - 1][j-2] + arr[i-2][j - 1]
print(arr[n][m])