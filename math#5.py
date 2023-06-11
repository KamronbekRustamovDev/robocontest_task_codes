from math import*
a,b=map(int,input().split())
s=(3**(0.5))/2
k=log(a,b)
z=a**2
v=2*b
q=z/v
x=s+k+q
print(format(x,".2f"))
