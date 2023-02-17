n, t = map(int, input().split())
tbl = [[0] * (n + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (n + 2)]
for _ in range(t):
    tmp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            s = sum([sum(k[j - 1 : j + 2]) for k in tbl[i - 1 : i + 2]]) - tbl[i][j]
            if s == 3 : 
                tmp[i][j] = 1
            elif s == 2: 
                tmp[i][j] = tbl[i][j]
    tbl = tmp
for i in range(1, n + 1): 
    print(*tbl[i][1 : n + 1])