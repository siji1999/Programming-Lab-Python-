n=int(input("enter a number"))
def fib(n):
    a=0
    b=1
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        return c

result=fib(n)
print(result)
fib(n)
