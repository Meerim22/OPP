n = 2 * 10 ** 7
IsPrime = [True] * (n + 1)
IsPrime[0] = False
IsPrime[1] = False
d = 2
while d * d <= n:
    if IsPrime[d]:
        for i in range(d * d, n + 1, d):
            IsPrime[i] = False
    d += 1
i = 1
count = 0
while count < 10 ** 6:
    i += 1
    if IsPrime[i]:
        count += 1
print(i)