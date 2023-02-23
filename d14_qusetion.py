a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
b=[]
d=[]
max=0
min=1000
while i<len(a):
    c=len(a[i])
    if c>max:
        max=c
        e=a[i]
        # b.append(e)
    if c<min:
        min=c
        f=a[i]
        # d.append(f)
    i=i+1
print(max,e)
print(min,f)  





















# list=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# i=1
# b=[]
# while i<len(list):
#     c=list[1][1],list[4]
#     b.append(c)
#     i=i+1
#     break
# print(b)


# l=[[[0],[1,3],[5,7],[9,11],[13,15,17]]]
# c=l[0]
# b=[]
# i=0
# while i<len(a):
#     if a[i]<c:
#         min=a[i]
#         b.append(min)
#     i=i+1
# print(b)
