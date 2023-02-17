n = int(input())
Primes = []
isPrime = [True]*(n+1)
for d in range(2,n+1):
    if isPrime[d]:
        Primes.append(d)
    for i in range(d*d, n+1,d):
        isPrime[i] = False
print(len(Primes))