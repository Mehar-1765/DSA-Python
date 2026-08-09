#delete a value in sll
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
n=int(input("Enter the size of SLL:"))
for i in range(n):
    value=int(input("Enter a value:"))
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
print("After inserting....")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("tail")
key=int(input("Enter the Element you want to delete:"))
if head is None:
    print("SLL Empty...")
elif head.data==key:
    head=head.next
else:
    temp=head
    while temp.next and temp.next.data!=key:
        temp=temp.next
    if temp.next:
        temp.next=temp.next.next
    else:
        print("Value not found....")
print("After deleting by value...")
temp=head
while temp:
        print(temp.data,end='->')
        temp=temp.next
print("tail")'''
