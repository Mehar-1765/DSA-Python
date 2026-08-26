# 2 sum
# Time complexity - O(n^2)
arr=list(map(int,input('Enter elements: ').split()))
target=int(input('Enter target: '))
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print('Pair found at index values: ',i,j)
            print('Pair: ',arr[i],arr[j])
            break
