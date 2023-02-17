n = int(input())
def factor(n):
    ans = []
    d = 2
    while d*d <= n:
        while n % d ==0:
            n //=d
            ans.append(d)
        d+=1
    if n !=1:ans.append(n)
    return ans
ans = factor(n)
an = set(ans)
s = []
for i in an:
    num = ans.count(i)
    if num == 1: r = str(i)
    else: r = str(i)+'^'+str(num)
    s.append(r)
x = '*'.join(s)
print(x)