#target sum using 2 pointer technique
# with sorting
# arr=list(map(int,input('Enter elements: ').split()))
# arr.sort()
# target=int(input('Enter target: '))
# left=0
# right=len(arr)-1
# print('After sorting array: ',arr)
# while left<right:
#     total=arr[left]+arr[right]
#     if total==target:
#         print('Pair found at',left,right)
#         print('Pair found is ',arr[left],arr[right])
#         break
#     elif total<target:
#         left+=1
#     else:
#         right-=1
# else:
#     print('No pair found')

# without sorting
# arr = list(map(int, input('Enter elements: ').split()))
# target = int(input('Enter target: '))
# found = False
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] + arr[j] == target:
#             print('Pair found at index', i, j)
#             print('Pair found is', arr[i], arr[j])
#             found = True
#             break
#     if found:
#         break
# if not found:
#     print('No pair found')

