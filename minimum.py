a=[3,5,25,1,3]
c=a[0]
b=[]
i=0
while i<len(a):
    if a[i]<c:
        min=a[i]
        b.append(min)
    i=i+1
print(b)
    