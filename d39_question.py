a=[[0,1,2],[2,3,4],[3,4,5,6],[7,8,9,10,11],[12,13,14]]
i=0
b=[]
while i<len(a):
    c=a[i]
    j=0
    sum=0
    while j<len(c):
        sum=sum+a[j][i]
        j=j+1
    b.append(sum)
    i=i+1
print(b)        


# i=41
# while i<57:
#     a=(i-40)
#     if i==16:
#         break
#     print(a)
#     i=i+1


# a=input("enter the number")
# i=a
# while i<=a:
#     j=i