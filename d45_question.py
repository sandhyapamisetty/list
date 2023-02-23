a=[2,3,9,8,2,0,39,84,2,2,34,2,34,2,34,5,3,5]
i=0
b=[]
n=int(input("enter"))
while i<len(a)-n:
    c=a[i]
    b.append(c)
    i=i+1
print(b)