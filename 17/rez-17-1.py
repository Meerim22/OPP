def f(x):
    d = set()
    i = 2
    while i*i<=x:
        while x%i == 0:
            x//=i
            d.add(i)
        i+=1
    if x>1: d.add(x)
    if len(d) <= 1: return 0
    if len(d) >1: return 1
k=100000
while True:
    k -= 1
    if str(k) ==str(k)[::-1]:
        m = f(k)
        if m == 0:
            print(k)
            break
    