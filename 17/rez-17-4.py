a,b = 99767158783375906672616888783904,78650768247942369971819788122060
def gcd(a,b):
    global count
    while b != 0:
        count += a//b
        a,b = b, a%b
count = 0
gcd(a,b)
print(count)