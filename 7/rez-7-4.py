s = int(input())
n = int(input())
rk, ch=0,0
for i in range(n):
    ves = int(input())
    if rk + ves <= s:
        rk += ves
    else:
        ch += ves
print(rk)
print(ch)