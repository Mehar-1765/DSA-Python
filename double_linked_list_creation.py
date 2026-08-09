#double linked list creation
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
head=None
tail=None
n=int(input('Enter DLL size: '))
for i in range(n):
    value=int(input('Enter a value: '))
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        newnode.prev=tail
        tail=newnode
print("Forword traversal:")        
temp = head
while temp:
    print(temp.data, end='<->')
    temp = temp.next
print("Tail")