N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
i = j = 0
m, s, ans = 0, 0, 10**9
while ans !=0 and i < N and j < M:
    if abs(A[i] - B[j]) < ans:
        ans = abs(A[i] - B[j])
        m = i
        s = j
    elif A[i] > B[j]:
        j += 1
    elif A[i] < B[j]:
        i += 1
else:
    print(A[m], B[s])