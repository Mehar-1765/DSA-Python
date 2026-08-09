# Bubble sort - it will check every adjucent element and if it is greater then it swap with the next element
# It is only for small systems
# TC - Best Case - O(n) Worst Case - O(n^2) SC - O(1)
n=list(map(int,input('Array elements: ').split()))
for i in range(len(n)-1):
    for j in range(len(n)-i-1):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
print(*n)