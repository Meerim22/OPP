a, b, c = map(int, input().split())
if a < 0:
    a += 1
t = a - b + c
if t <= 0:
    t -= 1
print(t)