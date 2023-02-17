ferz = input()
letters = 'abcdefgh'
m = letters.find(ferz[0])
n = int(ferz[1])
a = []
for i in range(8):
    b = []
    for j in range(8):
        if i == n and j == m:
            b.append("Q")
        elif i != n and j == m:
            b.append("*")
        elif i == n and j != m:
            b.append("*")
        elif abs(i-n) == abs(j-m):
            b.append("*")
        else:
            b.append(".")
    a.append(b)
for i in range(len(a)):
    print(*a[i])