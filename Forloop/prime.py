# m=int(input('enter start value(m):'))
# n=int(input('enter end value(n):'))
# for num in range(m,n+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num, end=" ")


#count all prime numbers
# m=int(input('enter start value(m):'))
# n=int(input('enter end value(n):'))
# count=0
# for num in range(m,n+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             count+=1
#             print(num, end=" ")
# print("count of prime numbers", count)


#print first prime number
m=int(input('enter start value(m):'))
n=int(input('enter end value(n):'))
for num in range(m,n+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num, end=" ")
            break



