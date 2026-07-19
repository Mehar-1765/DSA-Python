# square pattern
# n=int(input('Num: '))
# for i in range(n):
#     for j in range(n):
#         print('*',end=' ')
#     print()

# hallow square
# n=int(input('Num: '))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# hallow square with diagonals
# n=int(input('Num: '))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# hour glass
# n=int(input('Num: '))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or i==j or i+j==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# butterfly
# n=int(input('Num: '))
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-1 or i==j or i+j==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# into - *
# n=int(input('Num: '))
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# + - code
# n=int(input('Num: '))
# for i in range(n):
#     for j in range(n):
#         if i==n//2 or j==n//2 :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# hallow triangles
# hallow tilted right triangle
# n=int(input('Num: '))
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i+j==n-1 :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# hallow reverse right angle
# n=int(input('Num: '))
# for i in range(n):
#     for j in range(n):
#         if i==n-1 or j==n-1 or i+j==n-1 :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# hallow reverse tilted right triangle
# n=int(input('Num: '))
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==n-1 or i==j :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# hallow right angle
# n=int(input('Num: '))
# for i in range(n):
#     for j in range(n):
#         if i==n-1 or j==0 or i==j :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# T
# n=int(input('Num: '))
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==n//2:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# normal triangles
# n=int(input('Num: '))
# for i in range(1,n+1):
#     for j in range(i):
#         print('*',end=' ')
#     print()

# n=int(input('Num: '))
# for i in range(n,0,-1):
#     for j in range(i):
#         print('*',end=' ')
#     print()

# n=int(input('Num: '))
# for i in range(n,0,-1):
#     for j in range(i-1):
#         print(' ',end=' ')
#     for j in range(n-i+1):
#         print('*',end=' ')
#     print()

# n=int(input('Num: '))
# for i in range(1,n+1):
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(n-i+1)
#         print('*',end=' ')
#     print()