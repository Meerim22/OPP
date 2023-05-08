S = list(map(int, input().split()))
ans = [1] 
for i in range(len(S)):
    if S[i] % ans[-1] == 0: ans.append(S[i])
print(len(ans)-1)