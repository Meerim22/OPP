m = int(input())
a = list(map(int, input().split()))
sum=0
for i in range(len(a)-1):
    if int(a[i]+1) != int(a[i+1]):
        sum +=1
print(sum)