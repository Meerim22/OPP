from math import gcd
a,b = map(int, input().split())
r = (a*b)//(gcd(a,b))
print(r)