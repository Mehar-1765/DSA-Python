class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
head=None
tail=None
n=int(input("enter DLL size:"))
for i in range(n):
    value=int(input("enter a value:"))
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        newnode.prev=tail
        tail=newnode
print("forword traversal:")        
temp = tail
while temp:
    print(temp.data, end='<->')
    temp = temp.prev
print("tail")