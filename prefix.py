def precedence(op):
    if op=='+' or op=='-':
        return 1
    elif op=='*' or op=='/':
        return 2
    elif op=='^':
        return 3
    return 0
infix=input('Enter expression: ')
infix=infix[::-1]
stack=[]
postfix=''
for ch in infix:
    if ch.isalnum():
        postfix+=ch
    else:
        while stack and precedence(stack[-1])>precedence(ch):
            postfix+=stack.pop()
        stack.append(ch)
while stack:
    postfix+=stack.pop()
prefix=postfix[::-1]
print(prefix)