class stack:
    def __init__(self):
        self.stack=[]
        self.max_size=5
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
while True:
    if len(s.stack)==s.max_size:
        print('Stack overflow.......')
        break
    n=int(input('Enter value: '))
    s.stack.append(n)
    ch=input('Do you add another value(y/n): ')
    if ch.lower()=='n':
        break
print('Stack: ',s.stack)
s.pop()
s.pop()
print('Peek element: ',s.stack[-1])