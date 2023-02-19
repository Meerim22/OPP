n = list(map(str, input().split()))
stack = []
for i in n:
    if i != '+' and i != '-' and i != '*':
        stack.append(int(i)) 
    else:
        x,y = stack.pop(-2),stack.pop(-1)
        if i == '*': stack.append(x*y) 
        elif i == '-': stack.append(x-y) 
        elif i == '+': stack.append(x+y) 
print(*stack)