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
if len(ans) == 2 and len(an) == 2:
    print('YES')
else:
    print('NO')