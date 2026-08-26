# moving all zeros to the left using 2 pointer approach
# [0,1,0,3,0,2] -> [1,(3,2,0,0,0]
arr=list(map(int,input('Enter elements: ').split()))
slow=0
fast=0
for fast in range(len(arr)):
    if arr[fast]!=0:
        arr[slow],arr[fast]=arr[fast],arr[slow]
        slow+=1
print(arr)