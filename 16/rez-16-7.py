from math import gcd
x1,y1,x2,y2 = map(int, input().split())
m = gcd(abs(x1-x2), abs(y1-y2))
print(m+1)