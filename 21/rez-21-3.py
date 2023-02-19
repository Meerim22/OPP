s = input()
stack = []
for smb in s:
    if stack == []:
        stack.append(smb)
    elif smb == stack[-1]: stack.pop()
    else: stack.append(smb)
print(''.join(stack))