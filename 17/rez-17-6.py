n = int(input())
h=[]
deln = [0]*(n+1)
for d in range(2,n+1):
    for i in range(d*d, n+1,d):
        deln[i] +=1 
for i in range(len(deln)):
    if deln[i]> 3:
        h.append(i-2)
        print(i)
print(*h)