# a=[4,6,4,3,3,4,3,4,3,8]
# k=3
# b=[]
# i=0
# while i<len(a) :
#     c=a.count(a[i])
#     if c>k:
#         if a[i] not in b:
#            b.append(a[i])
#     i=i+1
# print(b)
    
    
a=[4,6,4,3,3,4,3,4,6,6]
i=0
k=2
b=[]
while i<len(a):
    c=a.count(a[i])
    if c>k:
        if a[i] not in b:
            b.append(a[i])
        i=i+1
print(b)
    