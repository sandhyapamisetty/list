sandhyalist =["my name is sandhya"]
# print(sandhyalist)
# sandhyalist.append("green")
# print(sandhyalist)
# sandhyalist.insert(4,"white")
# print(sandhyalist)
# sandhyalist.pop(5)
# print(sandhyalist)
# sandhyalist.remove("red")
# print(sandhyalist)
# sandhyalist.sort()
# print(sandhyalist)
sandhyalist.reverse()
print(sandhyalist)
# sandhyalist.copy()
# print(sandhyalist)
# print(sandhyalist.index("blue"))
# print(sandhyalist.count("red"))
# print(sandhyalist.clear())
# list=["sandhya","harika"]
# print(list[:])
# list=[100,90, 40,0,1]
# list.reverse()
# print(list)
# list=["sandhya","harika"]
# print(len(list))
# list=["sandhya","harika","bindu"]
# print(list[0:2]


# list=[3,2,5,7,3,6]
# list.pop(3)
# print(list)

# list1= [2, 33, 222, 14, 25]
# print(list[])


# list=[3,4,5,20,5,25,1,3]
# print(list.count(5))










# e.y=int(input("enter the year"))
# e.m=int(input("enter the month"))
# e.d=int(input("enter the day"))
# r.y=int(input("enter the year"))
# r.m=int(input("enter the month"))
# r.d=int(input("enter the day"))

# numbers=[50,40,23,70,12,5,7,10]
# count=1
# for elements in  numbers:
#     count=count+1
# print(count)

# list=[20,100,20,1,10]
# list.sort()
# print(list)
# print("the smallest number",list[0])
# print("the largest number",list[-1])



# a=[50,40,23,70,56,12,5,10,7]
# count=0
# i=0
# while i<(len(a)):
#     if a[i]>=20 and a[i]<=40:
#         count=count+1
#     i=i+1
# print(count)
   
   
   
# n=int(input("enter the number no of elements "))
# l=[]
# for i in range(n):
#     ele=int(input("enter the number"))
#     l.append(ele)
# print(l)
# # sorted_list=l.sort()
# print(sorted_list)
# maximum=l[-1]
# print("maximum",maximum)
# minimum=l[0]
# print("minimum",minimum)
# secondlargest=l[-2]
# print("second largest",secondlargest)


# n=int(input("enter the number"))
# i=1
# l=[]
# while  i<=n:
#     ele=int(input("enter the number"))
#     l.append(ele)
#     i=i+1
# print("l",l)
# b=l.sort()
# print(l)
# minmum=l[0]
# print("minmum",minmum)
# maxmium=l[-1]
# print("maxmium",maxmium)
# secondlargest=l[-2]
# print("second largest",secondlargest)



# places=["delhi","kurnool","gujarat","rajasthan","kerala"]
# print(places[::-1])


# n=int(input("enter the number"))
# l=[]
# for i in range(n):
#     ele=int(input("enter the elements"))
#     l.append(ele)
# print(l)
# print(l[::-1],end="")

# day=int(input("enter the number"))
# if day<=5:
#     print(day*2)
# elif day>=6 or day<10:
#     a=(5*2)+(day-5)*3
#     print(a)
# elif day>=10 or day<15:
#     b=(5*2)+(day-5)*3+(day-10)*4
#     print(b)
# elif day>=15:
#     c=(5*2)+(day-5)*3+(day-10)*4+(day-15)*5
#     print(c)
# else:
#     print("no")

# # # l=input("enter the number")
# # l=["m","a","d","a","m"]
# reverse=(l[::-1])
# # print(l)

# if reverse==l:
#     print("palidrom")
# else:
#     print("not palindrom")
    


# n=int(input("enter the number"))
# pal=n
# rev=0
# while n>0:
#     b=n%10
#     rev=rev*10+b
#     n=n//10
# print(rev)
# if rev==pal:
#     print("palindrom")
# else:
#     print("not palindrom")


# n=int(input("enter the number"))
# l=[]
# i=1
# while i<=n:
#     ele=int(input("enter the number"))
#     l.append(ele)
#     i=i+1
# print(l)
# b=l[::-1]
# if l==b:
#     print("pal")
# else:
#     print("not pal")

# a=int(input("enter the number"))
# b=0
# i=1
# while a!=0:
#     r=a%10
#     b=b+(r*i)
#     i=i*2
#     a=int(a/10)
# print(b)

# l=["f","g","c"]
# i=0
# index=0
# while i<len(l):
#     print(index,":",l[i])
#     index+=1
#     i=i+1


# l=["f","g","c"]

# index=0
# for i in range(len(l)):
#     print(index,":",l[i])
#     index=index+1

    

# l=[6,1,3,5,6,3,1] 
# n=[]
# for i in l:
#     if i not in n:
#         n.append(i)
# print(n)

# l=[6,1,3,5,6,3,1]
# n=[] 
# while i <len(l):
#     if i not in n:
#         n.append(i)
#     i=i+1
# print(n)
    
    
# l=[6,1,3,5,6,3,1]
# i=1
# n=[]

# while i<len(l):
#     if l[i] not in n:
#         n.append(l[i])
#     i=i+1
# print(n)
    
# l=[6,1,3,5,6,3,1]
# n=[]
# for i in l:
#     if i not in n:
#         n.append(i)
# print(n)
    
    
# l=[1,2,2,5,8,4,4,8] 
# n=[]
# i=0
# while i< len(l):
#     if l[i] not in n:
#         n.append(l[i])
#     i=i+1
# print(n)

# list=["sandhya","pavani"]
# n1,n2=list
# print(n1)
# print(n2)

# a=[3,4,5,20,5,25,1,3]
# c=[34,5]
# a.extend(c) 
# print(a)  

# a=[3,4,5,20,5,25,1,35]
# a.pop(1)
# print(a)    

# list1 = [8,0,9,5]
# print(list1[::-1])

# list1 = ["Python", "Java","c","C++","C"]
# print(min(list1))


# L=list("www.csiplearninghub.com")
# print(L[20:-1])

# list1=[1,3,5,2,4,6,2]
# list1.remove(2)
# print(sum(list1))

# L = [1,2,3,4,5]
# for i in L:
#     print(i,end=" ")
# i=i+1

# L = [1,2,3,4,5]
# for i in L:
#     print(i,end=" ")
# i=i+1



# a=[1,3,2]
# c=a*2
# print(c)

# a=[1,3,2]
# i=0
# b=[]
# while i<len(a):
#     c=a[i]*2
#     b.append(c)
#     i=i+1
# print(b)


# students = ['sandhya', 'bindu', 'radha', 'hari', 'akhila', 'jeevana']
# marks = [10, 20, 56, 45, 36, 20]
# count=0
# while count<len(students):
#     print(students[count],marks[count])
#     count=count+1


# a=[2,3,5,6,5,8,4,3,2,7]
# i=0
# b=[]
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     b.append(sum)
#     i=i+1
# print(b)


# a=[2,3,5,7]
# i=0
# b=[]
# while i<len(a):
#     c=sum(a)
#     b.append(c)
#     i=i+1
# print(b)


# a=[2,3,5,7]
# i=0
# c=1
# b=[]
# while i<len(a):
#     if a[i]not in b:
#        b.append(a[i])
#        c=c*a[i]
#     i=i+1
# print(c)

# i=-4
# while i<5:
#     i=i+1
#     if i==-3 or i==-2 or i==-1:
#         continue
#     print(i)

# a=[1,2,3,4,5,6,2,1]
# i=0
# while i<len(a):
#     b=(a[2],a[3],a[4],a[5])
#     i=i+1
# # print(b)
    
# a=[0,1,2,3,4,]
# b=("pen")
# a.extend(b)
# print(a)
