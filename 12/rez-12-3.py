def F(n):
    if n <= 2:
        return 1
    return F(n-1)+F(n-3)
print(F(int(input())))