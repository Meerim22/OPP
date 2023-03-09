n, x, y = map(int, input().split())
left, right = 0, min(x,y)*10**9
while left +1 < right:
    t = (right+left)//2
    if t//x +t//y < n-1: left = t
    else: right = t
print(right+min(x,y))