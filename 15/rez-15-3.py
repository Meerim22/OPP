def f(x):
    d = set()
    i = 2
    while i*i<=x:
        while x%i == 0:
            x//=i
            d.add(i)
        i+=1
    if x>1: d.add(x)
    return d.issubset({2,5,7})
k=0
for i in range(2,10000):
    if f(i) == True:
        k+=1
    if k == 100:
        print(i)
        break