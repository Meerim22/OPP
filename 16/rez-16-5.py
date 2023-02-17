n = int(input())
i = 2
k = 0
if n % i != 0:
    j = 3
    while j*j < n+1 :
        if n%j == 0:
            k = 1
            i = j
            break
        j += 2
else :
    k = 1
if k == 1:
    print(n//i, (i-1)*(n//i))
else :
    print(1, n-1)