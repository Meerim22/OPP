n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
mark = [0]*n 
def dfs(k,color):
    mark[k] = color
    for i in range(n):
        if A[k][i] == 1 and mark[i] == 0:
            dfs(i, color)
dfs(0,1)
tmp = 0
for i in range(n):
    tmp += sum(A[i])
if sum(mark) == n and tmp // 2 == n - 1:
    print('YES')
else:
    print('NO')