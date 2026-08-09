# Flip sort
# Pancake sort
#  TC - O(n^2)  SC - O(1)
arr=list(map(int,input('Enter elements: ').split()))
def flip(arr,k):
    left=0
    right=k
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
n=len(arr)
for curr_size in range(n,1,-1):
    max_index=0
    for i in range(1,curr_size):
        if arr[i]>arr[max_index]:
            max_index=i
    if max_index!=curr_size-1:
        flip(arr,max_index)
        flip(arr,curr_size-1)
print(*arr)