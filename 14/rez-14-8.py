A = input()
B = {}
for elem in A:
    B[elem] = B.get(elem,0)+1
print(B)