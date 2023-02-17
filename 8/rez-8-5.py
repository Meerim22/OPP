string = input()
x=0
num = '0123456789'
for i in string:
    if i in num:
        x+=1
if x > 0:
    print('domestic animal')
else:
    print('wild animal')