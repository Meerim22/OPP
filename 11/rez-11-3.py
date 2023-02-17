def summa(num):
    n = 0
    for i in num:
        m = int(i)
        n += m
    return n

n = int(input())
A = list(map(str, input().split()))
l, h = 0,0
for i in range(n):
    j = summa(str(A[i]))
    if j > h:
        h,l = j,A[i]
print(l)