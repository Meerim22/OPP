n, m = map(int, input().split())
a = [list([-1 for j in range(m)]) for i in range(n)]
a[0][0] = 1
def sol(i, j):
    if i >= 0 and j >= 0 and i < n and j < m:
        if a[i][j] == -1:
            a[i][j] = sol(i-2, j-1)+sol(i-2, j+1)+sol(i-1, j-2)+sol(i+1, j-2)
    else:
        return 0
    return a[i][j]
print(sol(n-1, m-1))

# arr = [[0 for j in range(m+2)] for i in range(n+2)]
# arr[1][1] = 1
# for i in range(2, n + 1):
#     for j in range(2, m + 1):
#         arr[i][j] = arr[i - 1][j-2] + arr[i+1][j - 2] + arr[i - 2][j-1] + arr[i-2][j + 1]
# print(arr[n][m])