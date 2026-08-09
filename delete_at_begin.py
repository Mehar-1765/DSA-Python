#delete at begin
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
print("forward traversal:")
temp = head
while temp:
    print(temp.data, end='<->')
    temp = temp.next
print("tail")
if head is None:
    print("DLL Empty..")
elif head.next is None:
    head=None
    tail=None
else:
    head=head.next
    head.prev=None
print("After delete at begin:")
temp = head
while temp:
    print(temp.data, end='<->')
    temp = temp.next
print("tail")