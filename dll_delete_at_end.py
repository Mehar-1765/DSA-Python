#DLL insert at end and delete at end:
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
        newnode.next=head
        head.prev=newnode
        head=newnode
print("forword traversal:")
temp = head
while temp:
    print(temp.data, end='<->')
    temp = temp.next
print("tail")

if head is None:
    print("DLL is empty")
elif head.next is None:
    head=None
    tail=None   
else:
    tail=tail.prev
    tail.next=None
print("After delete at end:")
temp=head
while temp:
    print(temp.data, end='<->')
    temp=temp.next
print("Tail")