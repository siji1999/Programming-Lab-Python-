l1=[1,2,3,4,5]
l2=[2,5,6,7,8,9]
a=len(l1)
b=len(l2)
if a==b:
    print("lengths are same")
else:
    print("lengths are not same")

s1=0
s2=0
for i in l1:
    s1=s1+1
for j in l2:
    s2=s2+1
if s1==s2:
    print("lists sums are same")
else:
    print("lists are not same")

p=set(l1)
q=set(l2)
r=p.intersection(q)
if r!=0:
    print("values in both list are:",r)

    
