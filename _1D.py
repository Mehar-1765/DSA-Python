# printing the given number into separate digits  

#1
# n=int(input('Num: '))
# while n!=0:
#     d=n%10
#     print(d)
#     n//=10

#2
# n=int(input('Num: '))
# l=[]
# while n!=0:
#     d=n%10
#     l.append(d)
#     n//=10
# print(*(l[::-1]))

#3
# n=int(input('Num: '))
# d=0
# while n!=0:
#     d+=n%10
#     n//=10
# print(d)

# n=int(input('Num: '))
# d=0
# i=1
# while i<=n:
#     d+=i/(i+1)
#     i+=1
# print(d)

# 7,6,14,12,21,18....
#Series printing
# n=int(input('Num: '))
# c=0
# for i in range(1,n+1):
#     if c==14:
#         break
#     else:
#         print(7*i,end=' ')
#         c+=1
#         print(6*i,end=' ')
#         c+=1

# 7,6,14,12,21,18....
# 14th term printing
# n=int(input('Num: '))
# c=0
# l=[]
# for i in range(1,n+1):
#     if c==14:
#         break
#     else:
#         l.append(7*i)
#         c+=1
#         l.append(6*i)
#         c+=1
# print(l[-1])