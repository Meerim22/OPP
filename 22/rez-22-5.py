n = int(input())
d = {}
for i in range(n):
    word,num = input().split()
    d.setdefault(num, []).append(word)
l = list(map(int,d.keys()))
l.sort()
for i in l:
    r = []
    for m in d[str(i)]:
        r.append(m)
    r.sort()
    for m in r:
        print(i,m)