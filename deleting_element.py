class stack:
    def __init__(self):
        self.stack=[]
    def pop(self):
        if len(self.stack)==0:
            print('Stack is empty.....')
        else:
            print('Deleted element: ',self.stack.pop())
            print('Stack after pop: ',self.stack)
    def push(self,item):
        self.stack.append(item)
        print('Stack after push: ',self.stack)
s=stack()
n=int(input("Enter size of stack: "))
for i in range(n):
    val=int(input('Enter value: '))
    s.stack.append(val)
s.pop()