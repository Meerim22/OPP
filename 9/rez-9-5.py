a = list(map(int, input().split()))
sum=0
for i in range(len(a)-1):
    sum += abs(a[i] - a[i+1])
print(sum)