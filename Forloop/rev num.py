# n=int(input('enter a value:'))
# rev=0
# while n>0:
#     d=n%10
#     rev=rev*10+d
#     n//=10
# print('rev number' ,rev)



#perfectnum
n=int(input('enter a number:'))
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print('perfect')
else:
    print('not ')
    
