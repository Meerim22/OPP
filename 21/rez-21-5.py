s = list(map(int, input().split()))
stack,m = [],0
for smb in s:
    if len(stack)< 3:
        stack.append(smb)
    elif stack[-1] == stack[-2] == smb:
        m += 1
        while len(stack)>0 and stack[-1] == smb:
            stack.pop()
            m+=1
    else: stack.append(smb)
print(m)