N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
i = j = 0
while i < N and j < M:
    if A[i] +1 == B[j] or A[i] == B[j] +1:
        print('YES')
        break
    elif A[i] > B[j]:
        j += 1
    elif A[i] < B[j]:
        i += 1
else:
    print('NO')