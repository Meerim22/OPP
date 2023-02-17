def total(x,y,z):
    n,m = 0,0
    if x == 1:
        n += 1
    else:
        m +=1
    if y == 1:
        n += 1
    else:
        m +=1
    if z == 1:
        n += 1
    else:
        m +=1
    r = max(n,m)
    if r == n:
        r = 1
    else:
        r = 0
    return r

x,y,z = map(int, input().split())
print(total(x,y,z))