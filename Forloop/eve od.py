#only for even and odd
# for i in range(1,101):
#     if i%2==0:
#         print(i)
# for i in range(1,101):
#         if i%2!=0:
#              print(i)



# #for even  and odd sum
# even=0
# odd=0
# for i in range(1,101):
#     if i%2==0:
#         print(i)
#         even+=i
# for i in range(1,101):
#         if i%2!=0:
#              print(i)
#              odd+=i
# print(even)
# print(odd)


m=int(input('enter a  1stvalue'))
n=int(input('enter a 2nd value'))
count=0
even=0
odd=0
for i in range(m,n+1):
    if i%2!=0:
        # even+=i
        print(i)
for i in range(m,n+1):
    if i%2==0:
        # odd+=i
        print(i)
    count+=1
# print(even,'even')
# print(odd,'odd')
print(count,'count')
    
