# a=[4,5,5,5,3,8]
# i=0
# b=[]
# while i<len(a):
#     c=a.count(a[i])
#     if c>=3:
#         if a[i] not in b:
#             b.append(c)
#     i=i+1
# print(b)

a=[1,1,1,64,23,64,22,22,22]
i=0
b=[]
while i<len(a):
    c=a.count(a[i])
    if c>=3:
        if a[i] not in b:
            b.append(a[i])
    i=i+1
print(b)


# a=[["g","f","g"],["i","s"],["b","e","s","t"]]
# b=[]
# for i in a:
#     s=" "
#     for j in i:
#         s+=j
#         b.append(s)
# print(b)



