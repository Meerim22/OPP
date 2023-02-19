s = input()
stack = []
for smb in s:
    if smb == '(' or smb == '[' or smb == '{':
        stack.append(smb)
    else:
        if len(stack) == 0:
            print('NO')
            break
        else: 
            if smb == '}' and stack[-1] == '{': stack.pop()
            if smb == ')' and stack[-1] == '(': stack.pop()
            if smb == ']' and stack[-1] == '[': stack.pop()
else:
    if len(stack) > 0:
        print('NO')
    else: print('YES')