def summa(s):
    a = int(input())
    if a != 0:
        s+=a 
        return summa(s)
    else:
        return s
print(summa(0))