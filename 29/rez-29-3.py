n, S = map(int,input().split())
A = list(map(int,input().split()))
F = [1] +[0]*S
for i in range(len(A)):
    for s in range(S, A[i] - 1, -1):
        if F[s - A[i]] == 1:
            F[s] = 1
while F[S] == 0:
    S -=1
print(S)