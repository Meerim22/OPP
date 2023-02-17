from math import gcd
n = 0
for i in range(10000, 100000):
    m = gcd(i, 92)
    if m == 1:
        n += 1
print(n)