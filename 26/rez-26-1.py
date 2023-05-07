def Sposob(x,y,N):
    if y==8:
        return N
    if x==1:
        return Sposob(2, y+1, N)
    if x==8:
        return Sposob(7, y+1, N)
    return (Sposob(x+1, y+1, N) + Sposob(x-1, y+1, N))
y, x = map(int, input().split())
print(Sposob(x,y,1))