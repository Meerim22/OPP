n = int(input())
h=[]
deln = [0]*(n+1)
isPrime = [True]*(n+1)
for d in range(2,n+1):
    if isPrime[d]:
        for m in range(d-1, n, d):
            deln[m+1] += 1
    for i in range(d*d, n+1,d):
        isPrime[i] = False
for i in range(len(deln)):
    if deln[i] >= 3:
        h.append(i)
print(*h)