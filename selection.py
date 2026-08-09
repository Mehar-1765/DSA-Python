# Selection sort
# TC - Best Case - O(n) Worst Case- O(n^2) SC - O(1)
n=list(map(int,input().split()))
for i in range(len(n)-1):
    min_index=i
    for j in range(i+1,len(n)):
        if n[j]<n[min_index]:
            min_index=j
    n[i],n[min_index]=n[min_index],n[i]
print(*n)