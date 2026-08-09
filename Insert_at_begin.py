# Insert at begin
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
n=int(input('Enter the size of CLL: '))
for i in range(n):
    data=int(input('Enter value: '))
    newnode=node(data)
    if head is None:
        head=newnode
        tail=newnode
        tail.next=head
    else:
        newnode.next=head
        head=newnode
        tail.next=head
print('CLL: ')
temp=head
while temp.next!=head:
    print(temp.data,end='->')
    temp=temp.next
print(temp.data,end='->')
print(head.data)