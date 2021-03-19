n=int(input("enter a number"))
def fact(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    return f
result=fact(n)
print(result)
fact(n)
