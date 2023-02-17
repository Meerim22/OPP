from math import gcd
A = [11531520, 62789636052, 227696832, 1078110000000, 1585584000000]
d = A[0]
for elem in A[1:]:
    d = gcd(d,elem)
print(d)