from math import*
a,b,c=map(int,input().split())
x=((-b+(b*b-4*a*c)**(0.5))/(2*a))
print(format(x,".3f"))
