def isPrime(n):
    ans = []
    d = 2
    while d*d <= n:
        while n % d ==0:
            n //=d
            ans.append(d)
        d+=1
    # if n !=1:
    #     ans.append(n)
    return ans
n = 6733107047
print(isPrime(n))