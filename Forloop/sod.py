n=int(input ('enter a number'))
sum_digit=0
while n>0:
    digit=n%10
    sum_digit+=digit
    n=n//10
print("s of d", sum_digit)



# product
n=int(input('enter a number'))
product_digit=1
while n>0:
    digit=n%10
    product_digit=product_digit*digit
    n=n//10
print("p of d", product_digit)