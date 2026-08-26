arr=list(map(int,input('Enter elements: ').split()))
for i in arr.copy():
    if i<0:
        arr.remove(i)
print(arr)