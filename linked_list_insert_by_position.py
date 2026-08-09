class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
n=int(input('Enter SLL size: '))
for i in range(n):
    val=int(input('Enter value: '))
    newnode=node(val)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
pos=int(input('Enter position: '))
val=int(input('Enter value: '))
newnode=node(val)
if pos==1:
    newnode.next=head
    head=newnode
else:
    temp=head
    for i in range(pos-2):
        temp=temp.next
    newnode.next=temp.next
    temp.next=newnode
print('\nAfter insertion at begin: ')
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print('tail')