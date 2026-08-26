# 1
# arr=list(map(int,input('Enter elements: ').split()))
# stack=[]
# stack.append(arr[1])
# stack.append(arr[3])
# for i in range(0,len(arr), 2):
#     print(arr[i],end=' ')
# while stack:
#     print(stack.pop(),end=' ')

# 2
arr=list(map(int,input('Enter elements: ').split()))
stack=[]
for i in range(0,len(arr), 2):
    print(arr[i], end=' ')
for i in range(1,len(arr), 2):
    stack.append(arr[i])
while stack:
    print(stack.pop(), end=' ')