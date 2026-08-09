# reverse an array without slicing - TC - O(n/2) -best case, O(n) - worst case SC - O(1)
# arr=list(map(int,input('Enter numbers: ').split()))
# left=0
# right=len(arr)-1
# while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
# print('Reversed array: ',arr)
# a=10
# print(id(a)) # garbage value - some space for a where the value stored in memory

# left rotate an array by 1 value - 1,2,3,4,5 to 2,3,4,5,1 (clockwise)
# arr=list(map(int,input('Enter array elements: ').split()))
# temp=arr[0]
# for i in range(len(arr)-1):
#     arr[i]=arr[i+1]
# arr[-1]=temp
# print(arr)

# right rotate an array by 1 value - 1,2,3,4,5 to 5,1,2,3,4 (anti- clockwise)
# arr=list(map(int,input('Enter array elements: ').split()))
# temp=arr[-1]
# for i in range(len(arr),0,-1):
#     arr[i-1]=arr[i-2]
# arr[0]=temp
# print(arr)

# max num in array
# arr=list(map(int,input('Enter array elements: ').split()))
# l=arr[0]
# for i in range(len(arr)):
#     if l<arr[i]:
#         l=arr[i]
# print(l)

# small num in array
# arr=list(map(int,input('Enter array elements: ').split()))
# s=arr[0]
# for i in range(len(arr)):
#     if s>arr[i]:
#         s=arr[i]
# print(s)

# pattern in spiral clockwise - TC - O(n) SC - O(n)
# n=int(input('Size of matrix: '))
# arr=[[0]*n for _ in range(n)]
# print(arr)
# top=0
# left=0
# right=n-1
# bottom=n-1
# num=1
# while left<=right and top<=bottom:
#     # in top, left -> right
#     for i in range(left,right+1):
#         arr[top][i]=num
#         num+=1
#     top+=1
#     # in right, top -> bottom
#     for i in range(top,bottom+1):
#         arr[i][right]=num
#         num+=1
#     right-=1
#     # in bottom, right -> left
#     for i in range(right,left-1,-1):
#         arr[bottom][i]=num
#         num+=1
#     bottom-=1
#     # in left, bottom -> top
#     for i in range(bottom,top-1,-1):
#         arr[i][left]=num
#         num+=1
#     left+=1
# for row in arr:
#     print(*row)

# # Traversal of above matrix
# n=int(input('Size of matrix: '))
# arr=[[0]*n for _ in range(n)]
# print(arr)
# matrix=[]
# for i in range(n):

#     row=list(map(int,input().split()))
#     matrix.append(row)
# top=0
# left=0
# right=n-1
# bottom=n-1
# num=1
# while left<=right and top<=bottom:
#     # in top, left -> right
#     for i in range(left,right+1):
#         print(matrix[top][i],end='  ')
#         num+=1
#     top+=1
#     # in right, top -> bottom
#     for i in range(top,bottom+1):
#         print(matrix[i][right],end='  ')
#         num+=1
#     right-=1
#     # in bottom, right -> left
#     for i in range(right,left-1,-1):
#         print(matrix[bottom][i],end='  ')
#         num+=1
#     bottom-=1
#     # in left, bottom -> top
#     for i in range(bottom,top-1,-1):
#         print(matrix[i][left],end='  ')
#         num+=1
#     left+=1


# Traversal of above matrix
# n=int(input('Size of matrix: '))
# matrix=[]
# for i in range(n):
#     for j in range(n):
#         value=list(map(int,input().split()))
#         matrix.append(value)
# print(matrix)
# top=0
# left=0
# right=n-1
# bottom=n-1
# num=1
# while left<=right and top<=bottom:
#     # in top, left -> right
#     for i in range(left,right+1):
#         print(matrix[top][i],end='  ')
#         num+=1
#     top+=1
#     # in right, top -> bottom
#     for i in range(top,bottom+1):
#         print(matrix[i][right],end='  ')
#         num+=1
#     right-=1
#     # in bottom, right -> left
#     for i in range(right,left-1,-1):
#         print(matrix[bottom][i],end='  ')
#         num+=1
#     bottom-=1
#     # in left, bottom -> top
#     for i in range(bottom,top-1,-1):
#         print(matrix[i][left],end='  ')
#         num+=1
#     left+=1

# searching in arrays
# 1 Exract the index - TC - Best case-O(1) Worst case - O(n) SC - O(1)
# arr=list(map(int,input('Enter array elements: ').split()))
# n=int(input('Enter number to search index: '))
# c=0
# for i in range(len(arr)):
#     if arr[i]==n:
#         print('Element found at index: ',i)
#         break
#     elif arr[i]!=n and i==(len(arr)-1):
#         print('Element not found')

# TC - Best case-O(1) Worst case - O(n) SC - O(1)
# arr=list(map(int,input("enter the elements:").split()))
# target=int(input("enter the target:"))
# found=False
# for i in range(len(arr)):
#     if arr[i]==target:
#         print("index of target:",i)
#         found=True
#         break
# if not found:
#     print("target not found")

# first occurrence - TC - Best case - O(1) Worst case - O(n) SC - O(1)
# arr=list(map(int,input("enter the elements:").split()))
# target=int(input("enter the target:"))
# found=-1
# for i in range(len(arr)):
#     if arr[i]==target:
#         found=i
#         print("First occurrence of target:",i)
#         break
# if found==-1:
#     print("Target not found")

# First repeated occurrence - TC - Best case - O(2) Worst case - O(n) SC - O(1)
# arr=list(map(int,input("enter the elements:").split()))
# target=int(input("enter the target:"))
# found=-1
# c=0
# for i in range(len(arr)):
#     if arr[i]==target:
#         found=i
#         c+=1
#         if c==2:
#             print("First repeated occurrence of target:",i)
#             break
# if c<2:
#     print("Target not found")

# last repeated occurrence - TC - Best case - O(1) Worst case - O(n) SC - O(1)
# arr=list(map(int,input("enter the elements:").split()))
# target=int(input("enter the target:"))
# found=-1
# for i in range(len(arr)):
#     if arr[i]==target:
#         found=i
# if found==-1:
#     print("Target not found")
# else:
#     print('Last occurrence of the target: ',found)

# Counting the no of occurrences of the target - TC - O(n) SC - O(1)
# arr=list(map(int,input("enter the elements:").split()))
# target=int(input("enter the target:"))
# c=0
# for i in range(len(arr)):
#     if arr[i]==target:
#         c+=1
# if c==0:
#     print("Target not found")
# else:
#     print('Count of no of occurrence of the target: ',c)

# largest number in an array
# arr=list(map(int,input("enter the elements:").split()))
# lar=arr[0]
# for i in range(len(arr)):
#     if lar<arr[i]:
#         lar=arr[i]
# print("Largest element: ",lar)

# largest number index in an array
# arr=list(map(int,input("enter the elements:").split()))
# lar=arr[0]
# f=-1
# for i in range(len(arr)):
#     if lar<arr[i]:
#         lar=arr[i]
#         f=i
# print("Largest element index: ",f)

# smallest number in an array
# arr=list(map(int,input("enter the elements:").split()))
# sma=arr[0]
# for i in range(len(arr)):
#     if sma>arr[i]:
#         sma=arr[i]
# print("Smallest element: ",sma)

# smallest number index in an array
# arr=list(map(int,input("enter the elements:").split()))
# sma=arr[0]
# f=-1
# for i in range(len(arr)):
#     if sma>arr[i]:
#         sma=arr[i]
#         f=i
# print("Smallest element index: ",f)

# missing number search
# arr=list(map(int,input("enter the elements:").split()))
# f=-1
# for i in range(len(arr)):
#     if (i+1)!=arr[i]:
#         f=i+1
# print("Missing element: ",f)

# arr=list(map(int,input("enter the elements:").split()))
# n=len(arr)+1
# expected=n*(n+1)//2
# actual=sum(arr)
# print('Missing number: ',expected-actual)

# # pair search - first 
# arr=list(map(int,input("enter the elements:").split()))
# n=int(input('Num: '))
# f=-1
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if n==arr[i]+arr[j]:
#             f=1
#             print('Pair found at index: ',i,j)
#             print('Pair is: ',arr[i],arr[j])
#             break
#     if f==1:
#         break
# if f==-1:
#     print('Pair not found')


# pairs search - many
# arr=list(map(int,input("enter the elements:").split()))
# n=int(input('Num: '))
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         if n==arr[i]+arr[j]:
#             print(arr[i],arr[j])
