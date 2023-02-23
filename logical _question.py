# a=[1,2,3,4,5,6]
# i=0
# j=-1
# b=[]
# while i<3:
#     c=a[i]
#     k=a[j]
#     b.append(k)
#     b.append(c)
#     j=j-1
#     i=i+1
# print(b)
    
# a=[1,2,3,4,5,6]
# i=0
# while i<len(a):
#     c=a[0]=a[-1]
#     a[-1]=a[2]
#     a[2]=a[-2]
#     a[-2]=a[3]
#     a[3]=a[1]
#     a[-5]=a[-6]
#     i=i+1
# print(a)


# a=['sandhya','bindu']
# i=0
# b=''
# while i<len(a):
#     b=a[i][0]
#     i=i+1
#     print(b,end="")
   
   
# a=['bindu is singing very loudly']
# # i=0
# b=split(a)
# # while i<len(a):
# #     if a[i]!=very:
# #         b.append(a[i])
# #     i=i+1
# print(b)

# a=['sandhya','bindu','radha']
# i=0
# b=[]
# while i<len(a):
#     c=a[i][0]
#     b.append(c)
#     i=i+1
# print(b,",",end="")
        
   
# a=[1,2,3,4]
# b=emp
# c=str(b)
# i=0
# while i<len(a):
#     i=i+1
# print(c+a[i])
         
         
         
a=[1,2,3,4]
i=0
b=[]
while i<len(a):
    c=a[i-1]+a[i-2]
    b.append(c)
    i=i+1
print(b)


