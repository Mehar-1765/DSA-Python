# insert at begin
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input('Enter SLL size: '))
for i in range(n):
    val=int(input('Enter value: '))
    newnode=node(val)
    newnode.next=head
    head=newnode
temp=head
print('\nAfter insertion at begin: ')
while temp:
    print(temp.data,end='->')
    temp=temp.next
print('tail')
if head is None:
    print('SLL Empty')
elif head.next is None:
    head=None
else:
    temp=head
    while temp.next.next:
        temp=temp.next
    temp.next=None
print('\nAfter deletion at end: ')
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print('tail')