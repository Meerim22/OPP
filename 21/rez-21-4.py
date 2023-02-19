def push(x):
    stack.append(x)
    print('ok')
def pop():
    if  stack == []: print('error')
    else:
        x = stack.pop()
        print(x)
def back():
    if  stack == []: print('error')
    else: print(stack[-1])
def size():
    print(len(stack))
def clear():
    stack[:] = []
    print('ok')
def exit():
    print('bye')

stack, hehe = [],[]
n = input()
while n != 'exit':
    hehe.append(n)
    n = input()
for n in hehe:
    if n[0:4] == 'push': push(n[5:])
    elif n == 'pop': pop()
    elif n == 'back': back()
    elif n == 'size': size()
    elif n == 'clear': clear()
exit()