a=['a','b','c','d','e','f','g','h']
i=0
b=[]
c=[]
while i<len(a):
    n=a[i]
    if n>a[2]:
        b.append(n)
    else:
        c.append(n)
    i=i+1
s=b+c
print(s)    