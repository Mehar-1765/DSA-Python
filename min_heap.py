#heapify
# import heapq
# arr=list(map(int,input('Enter elements: ').split()))
# heapq.heapify(arr)
# print(arr)
# heapq.heappush(arr,0)
# heapq.heapify(arr)
# print(arr)
# x=heapq.heappop(arr)
# print('poped element: ',x)
# print(arr)

# import heapq
# arr=list(map(int,input('Enter elements: ').split()))
# x=heapq.heappushpop(arr,3)
# print('Removed element: ',x)
# print('heap: ',arr)
# heapq.heapify(arr)

# y=heapq.heapreplace(arr,10)
# print('Removed: ',y)
# print('heap: ',arr)

# z=heapq.nsmallest(2,arr)
# print(z)

# z=heapq.nlargest(2,arr)
# print(z)


#heapmerge method
import heapq
arr1=list(map(int,input('Enter elements: ').split()))
arr2=list(map(int,input('Enter elements: ').split()))
arr3=list(map(int,input('Enter elements: ').split()))
output=heapq.merge(arr1,arr2,arr3)
print(list(output))