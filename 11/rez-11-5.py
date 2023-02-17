def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

x1, y1, x2, y2, x3, y3 = map(int, input().split())
n1 = distance(x1, y1, x2, y2)
n2 = distance(x2, y2, x3, y3)
n3 = distance(x3, y3, x1, y1)
print(n1+n2+n3)