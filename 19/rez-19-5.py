def math(a):
    return a[0]/a[1]
def BubbleSort(A):
    n = len(A)
    for j in range(n-1,0,-1):
        for i in range(j):
            if math(A[i]) == math(A[i+1]):
                if A[i][0] > A[i+1][0]:
                    A[i] , A[i+1] = A[i+1], A[i]
            elif math(A[i]) > math(A[i+1]):
                A[i] , A[i+1] = A[i+1], A[i]
    return A
n = int(input())
A = [list(map(int, input().split('/'))) for i in range(n)]
A = BubbleSort(A)
for i in A:
    print(str(i[0])+'/'+ str(i[1]))