a=[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
i=0
b=[]
while i<len(a):
    j=0
    c=[]
    while j<=len(a[i]):
        c.append(a[j][i])
        j=j+1
    b.append(c)
    i=i+1
print(b)    