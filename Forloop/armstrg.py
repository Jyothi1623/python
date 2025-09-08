# n=int(input('enter a n:'))
# temp=n
# s=0
# while  temp>0:
#     d=temp%10
#     s+=d**3
#     temp//=10
# if s==n:
#         print('it is armstrong')
# else:
#       print("not armstrong")
 


#neon num
# n=9
# temp=n*n 
# s=0
# while temp>0:
#     d=temp%10
#     s+=d
#     temp//=10
# if s==n:
#     print('neon')
# else:
#     print('not neon')






#print all armstrng number
m=int(input('enter a value'))
n=int(input('enter a end value:'))
for i in range(m,n+1):
    temp=i
    total=0
    power=len(str(i))
    if power==1 and i!=1:
        continue
    while temp>0:
        d=temp%10
        total+=d**power
        temp//=10
    if total==i:
        print(i, end=" ")




