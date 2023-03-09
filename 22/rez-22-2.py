from collections import deque

def push(x):
    stack.append(x)
    print('ok')
def pop():
    x = stack.popleft()
    print(x)
def front():
    print(stack[0])
def size():
    print(len(stack))
def clear():
    stack[:] = []
    print('ok')
def exit():
    print('bye')

stack, hehe = deque(),[]
n = input()
while n != 'exit':
    hehe.append(n)
    n = input()
for n in hehe:
    if n[0:4] == 'push': push(n[5:])
    elif n == 'pop': pop()
    elif n == 'front': front()
    elif n == 'size': size()
    elif n == 'clear': clear()
exit()