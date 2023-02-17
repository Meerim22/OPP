A = list(map(int, input().split()))
m = 0
for i in range(len(A)):
    if A[i] < x:
        print(i+1)
        m +=1
        break
if m == 0: print(len(A)+1)