n = input()
a = list(map(int, input().split()))
m = a[0]
s = a.index(max(a))
a[0] = max(a)
a[s] = m 
print(*a)