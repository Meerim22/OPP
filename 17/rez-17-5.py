a = int(input())
b = int(input())
def s(a,b):
    Primes = []
    isPrime = [True]*(b+1)
    for d in range(2,b+1):
        if isPrime[d]:
            if a<=d<=b:
                Primes.append(d)
            for i in range(d*d, b+1,d):
                isPrime[i] = False
    return len(Primes)
print(s(a,b))