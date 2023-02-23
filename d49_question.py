a=['s','d','f','s','d','f','s','f','k','o','p','i','w','e','k','c']
i=0
while i<len(a):
    if a[i]=='f':
        s=i
    elif a[i]=='c':
        d=i
    elif a[i]=='k':
        e=i
    elif a[i]=='w':
        m=i
    i=i+1
print("last occurence f is:",s)
print("last occurence c is :",d)
print("last occurrencre k is :",e)
print("last occurrence w is :",m)
    
    