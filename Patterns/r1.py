
# def prime(n):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         return True
# n=int(input('enter a value'))             
# print(prime(n))

n=[1,1,2,3,3]
new=[]
for i in n:
    if  i not in new:
        new.append(i)
print(new)

    


    

