n = input()
a = list(map(int, input().split()))
rmin, rmax = a.index(min(a)),a.index(max(a))
m = a[rmin]
a[rmin] = a[rmax]
a[rmax] = m
print(*a)