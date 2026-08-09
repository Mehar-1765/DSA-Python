#insert at end
class node:
    def __init__(self, data):
        self.data=data
        self.next= None
head=node(10)
second=node(20)
third=node(30)
head.next=second
second.next=third
temp=head
while temp:
    print(temp.data, end='->')
    temp=temp.next
print("tail")
if head is None:
    print('SLL Empty: ')
else:
    head=head.next
print('\nAfter delete from begining: ')
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print('tail')