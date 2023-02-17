def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

a, b = 1024,346
m = gcd(a,b)
if (a+b+2) %2 == 0:
    print((a+b+2)-(m*2))
else:
    print((a+b+3)-(m*2))