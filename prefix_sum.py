#prefix sum
# arr=list(map(int,input("enter elements:").split()))
# prefix=[0]*len(arr)
# print(prefix)
# prefix[0]=arr[0]
# for i in range(1,len(arr)):
#     prefix[i]=prefix[i-1]+arr[i]
# print(prefix)

# prefix sum end
arr=list(map(int,input("enter elements:").split()))
prefix=[0]*len(arr)
print(prefix)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
print(prefix)
start=int(input('Enter start: '))
end=int(input('Enter end: '))
if start==0:
    result=prefix[end]
else:
    result=prefix[end]-prefix[start-1]
print('Range sum: ',result)