a=[1,2,3,4,5,6]
i=0
b=[]
while i<len(a)-1:
    k=[a[i],a[i+1]]
    b.append(k)
    i=i+1
print(b)