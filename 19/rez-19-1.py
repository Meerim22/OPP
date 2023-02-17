def sm(a):
    a = str(a)[1:-1]
    m=0
    for i in a:
        m += int(i)
    return m

A = [i for i in range(100,10001)]
A.sort(key=sm)
print(A)
print(A[2018])