n, r = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

i, j, count = 0, 1, 0
 
while j < n and i < n - 1:
    print(i,j,count)
    if i == j: j += 1
    elif a[j] - a[i] > r: j += 1
    else:
        count += 1
        i += 1
print(count)