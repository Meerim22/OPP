def O(a,logn):
    if logn%2 == 0:
        return (a**2)**(logn//2)
    else:
        return (a**(logn-1))*a
print(O(float(input()),float(input())))