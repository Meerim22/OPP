def select_sort(A):
    n=0
    for i in range(len(A) - 1):
        min_index = i
        for k in range(i + 1, len(A)):
            if A[k] < A[min_index]:
                min_index = k
                n+=1
        A[i], A[min_index] = A[min_index], A[i]
    return n
        
A =[3,5,2,4,6,1,8,9,7]
m = select_sort(A)
print(m)