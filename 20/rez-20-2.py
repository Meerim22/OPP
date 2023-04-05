n = input()
D = dict()
Count = list(map(int, input().split()))
Count.sort()
for elem in Count:
    D[elem] = D.get(elem,0)+1
Count = []
for elem in D:
    if D[elem] == 1:
        Count.append(elem)
print(*Count)