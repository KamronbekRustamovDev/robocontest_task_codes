a,b,c=map(int,input().split())
m=max(a,b,c)
mi=min(a,b,c)
if a<m and a>mi:
  print(mi,a,m)
elif b<m and b>mi:
  print(mi,b,m)
elif c<m and c>mi:
  print(mi,c,m)
else:
  print(a,b,c)
