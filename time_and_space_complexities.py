# print('Hi') # tc - O(1) sc - O(1) 

# a=1
# b=2
# print(a+b) # tc - O(1) sc - O(1) 

# n=int(input('Num: '))
# for i in range(n):
#     print(i) # tc - O(n) sc - O(1) 

# n=int(input('Num: '))
# for i in range(n):
#     print(i,'@') # tc - O(n) sc - O() 

# n=int(input('Num: '))
# for i in range(n):
#     print('@') 
# for i in range(n):
#     print('%') # tc - O(2n) sc - O(1)

# n=int(input('Num: '))
# l=[]
# for i in range(n):
#     l.append(i) # tc - O(n) sc - O(n)

# n=int(input('Num: '))
# while n>1:
#     print(n)
#     n//=2
# print(n) # tc - O(log(n)) sc - O(1)

# n=int(input('Num: '))
# while n>2:
#     print(n)
#     n=int(n**0.5)
# print(n) # tc - O(log(log(n))) sc - O(1)
n=int(input('Num: '))
for i in range(n):
    for j in range(i):
        print('*',end=' ')