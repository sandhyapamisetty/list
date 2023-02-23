a=[1,2,3,1,2,2]
i=0
b=[]
while i<len(a):
    c=a[i]
    if c not in b:
        b.append(c)
    i=i+1
print(b)