# Time Complexity
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n²)
# Space Complexity: O(log n) on average, O(n) in the worst case.

def part(arr,low,high):
    piv=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<piv:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quick_sort(arr,low,high):
    if low<high:
        piv=part(arr,low,high)
        quick_sort(arr,low,piv-1)
        quick_sort(arr,piv+1,high)
arr=list(map(int,input('Enter elements: ').split()))
quick_sort(arr,0,len(arr)-1)
print(*arr)