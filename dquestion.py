l=[6,1,3,5,6,3,1]
i=0
b=[]
while i<len(l):
    if l[i]not in b:
       b.append(l[i])
    i=i+1
print(b)
i=0
p=1
while i<len(b):
    p=p*b[i]
    i=i+1
print(p)    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
