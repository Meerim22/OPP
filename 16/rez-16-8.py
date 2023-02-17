def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
m = gcd(abs(x1-x2), abs(y1-y2))
print(abs(x1-x2)+abs(y1-y2)-d)