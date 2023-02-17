n, m, k = map(int, input().split())
A = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
for i in range(k):
    k1, k2 = map(int, input().split())
    A[k1][k2] = '*'
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i][j] == '*':
            pass
        else:
            amount = 0
            for d in range(j - 1 , j + 2):
                if A[i][d] == '*':
                    amount += 1
                if A[i+1][d] == '*':
                    amount += 1
                if A[i-1][d] == '*':
                    amount += 1
            A[i][j] = amount
for i in range(1, n+1): 
    print(*A[i][1 : m+1])

# n, m, k = map(int, input().split())
# A = [[0]*m for i in range(n)]
# for i in range(k):
#     k1, k2 = map(int, input().split())
#     A[k1-1][k2-1] = '*'
# for i in range(n):
#     for j in range(m):
#         if A[i][j] == '*':
#             pass
#         else:
#             amount = 0
#             if i != 0 and j != 0 and j != m-1:
#                 for d in range(-1,2):
#                     if A[i-1][j+d] == '*':
#                         amount += 1
#             if i != 0 and j == 0 and j != m-1:
#                 for d in range(0,2):
#                     if A[i-1][j+d] == '*':
#                         amount += 1
#             if i != 0 and j != 0 and j == m-1:
#                 for d in range(-1,1):
#                     if A[i-1][j+d] == '*':
#                         amount += 1
#             if j != 0 and j != m-1:
#                 for d in range(-1,1,2):
#                     if A[i][j+d] == '*':
#                         amount += 1
#             if j == 0:
#                 if A[i][j+1] == '*':
#                     amount += 1
#             if j == m-1:
#                 if A[i][j-1] == '*':
#                     amount += 1
#             if i != n-1 and j != 0 and j != m-1:
#                 for d in range(-1,2):
#                     if A[i+1][j+d] == '*':
#                         amount += 1
#             if i != n-1 and j == 0 and j != m-1:
#                 for d in range(0,2):
#                     if A[i+1][j+d] == '*':
#                         amount += 1
#             if i != n-1 and j != 0 and j == m-1:
#                 for d in range(-1,1):
#                     if A[i+1][j+d] == '*':
#                         amount += 1
#             A[i][j] = amount
# for row in A:
#     for elem in row:
#         print(elem, end=' ')
#     print()