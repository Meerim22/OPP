def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
n = int(input())
ans = 0
xfirst, yfirst = map(int, input().split())
xprev, yprev = xfirst, yfirst
for i in range(n - 1):
    x, y = map(int, input().split())
    ans += gcd(abs(x - xprev), abs(y - yprev))
    xprev, yprev = x, y
ans += gcd(abs(x - xfirst), abs(y - yfirst))
print(ans)