# a=int(input("enter the number"))
# b=[]
# i=len(str(a))-1
# for k in str(a):
#     if k!="0":
#         b.append(k+"0"*i)
#     i=i-1
#     x="+".join(b)
# print(" "+x+" ")    
    
    
a=int(input("enter the number"))
i=len(str (a))-1
b=[]
k=0
while k<len(str(a)):
    if k!="0":
        b.append(k+0*i)
    i=i-1 
    x="+".join(b)
print(" "+x+" ")
   
    