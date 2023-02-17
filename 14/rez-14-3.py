
a = set(map(int, input().split()))
b = set(map(int, input().split()))
number = len(a.difference(b))
print(number)