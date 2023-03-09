m, n = map(int, input().split())
A=[]
left, right = -1, 1000*200
for i in range(n):
    l = list(map(int, input().split()))
    A.append(l)
while left +1 < right:
    t = (right+left)//2
    s = 0
    for i in A:
        rest = (t//(i[0]*i[1]+i[2]))*i[2]
        s+= (t-rest)//i[0]
    if s < m: left = t
    else: right = t
print(right)