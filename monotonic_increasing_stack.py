arr=list(map(int,input('Enter elements: ').split()))
stack=[]
for i in arr:
    while stack and stack[-1]>i:
        stack.pop()
    stack.append(i)
print(*stack)