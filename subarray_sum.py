#sliding sum / subarray sum
arr = list(map(int, input('Enter elements: ').split()))
k=int(input("enter slide: "))
windowsum=sum(arr[:k])
maxsum=windowsum
for i in range(k,len(arr)):
    windowsum=windowsum-arr[i-k]+arr[i]
    if windowsum>maxsum:
        maxsum=windowsum
print(maxsum)