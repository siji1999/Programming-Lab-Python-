n=int(input("enter  current year"))
m=int(input("enter  final year"))
print("leaps years from ",n," to ",m," are:")
for i in range(n,m+1):
      
    if i%4==0:
        print(i)
n=int(input("enter the final year"))
for i in range(2021,n+1):
    if i%4==0:
        print(i)
