# Selection sort
# TC - Best Case - O(n) Worst Case- O(n^2) SC - O(1)
n=list(map(int,input().split()))
for i in range(1,len(n)):
    x=n[i]
    j=i-1
    while j>=0 and n[j]>x:
        n[j+1]=n[j]
        j-=1
    n[j+1]=x
print(*n)