def BubbleSort(A, B): 20-3
     for j in range(len(A) - 1, 0, -1):
        for i in range(0, j):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                B[i], B[i + 1] = B[i + 1], B[i]
A = [5, 1, 1, 2, 5, 3, 4, 8, -9, 0]
B = [5, 4, 1, 2, 3, 8, 0, 2, 7, 1]
BubbleSort(A, B)
print(*A)
print(*B)