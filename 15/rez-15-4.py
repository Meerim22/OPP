n=int(input())
k=2
while k*k<=n:
    if n%k==0:
       print(n//k)
       break
    k+=1
else:
    print(1)