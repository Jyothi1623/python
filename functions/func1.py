# # default arguement
# def power(x,y=3):
#     return x**y
# print(power(3))

# # keyword
# print(power(y=7,x=4))


# # multiple return 
# def s(a,b):
#     return a+b,a-b,a*b,a%b
# print(s(8,4))

# # variable len args
# def t(*a):
#     # return sum(a)
#     return min(a)

#     # return max(a)
#     # return len(a)

# print(t(2,76,8,98,67,45))


# keyword variable args
# def c(**j):
#     print(j)
# c(name='sravana',age=12)


# recursive
# def fact(n):
#     return 1 if n==1 else n*fact( n-1)
# print(fact(5))


# lamda fun
# s= lambda x:x*x
# print(s(5))

def calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "Invalid"

num1 = int(input("A: "))
num2 = int(input("B: "))
op = input("Enter + - * /: ")

print("Result =", calc(num1, num2, op))







