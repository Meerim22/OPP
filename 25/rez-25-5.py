n = int(input())
q=[0,1,1,1] + [0]*(n-3)

for i in range(4,n+1):
    if i % 3 ==0:
        q[i] = min(q[i//3], q[i-1]) + 1
    elif i % 2==0:
        q[i] = min(q[i//2], q[i-1]) + 1
    else:
        q[i] = q[i-1] + 1
 
print(q[n])

# n = int(input())
# m =0
# while n != 1:
#     if n % 3 ==0 :
#         n = n // 3
#         m+=1
#         print(1, n)
#     elif (n - 1) % 3 ==0:
#         n = (n - 1)//3
#         m+=2
#         print('01', n)
#     elif n % 2 == 0: 
#         n = n // 2
#         m+=1
#         print(2, n)
#     elif (n - 1) % 2 ==0:
#         n = (n - 1)//2
#         m+=2
#         print('02', n)
# print(m)