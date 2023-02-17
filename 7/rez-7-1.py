n = int(input())
t = ''
for i in range(1, n+1):
    x = i ** 2
    if n >= x:
        t += str(x) + ' '
    else:
        break
print(t)