n = input()
Clava = list(map(int, input().split()))
m = input()
Count = list(map(int, input().split()))
for elem in Count:
    Clava[elem-1] -= 1
for elem in Clava:
    if elem < 0:
        print('YES')
    else:
        print('NO')