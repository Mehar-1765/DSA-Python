#update a value in SLL with the given value        
class node:
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
old=int(input("Enter the element you want to update:"))
new=int(input("Enter the Element you want to update with:"))
temp=head
while temp:
    if temp.data==old:
        temp.data=new
        break
    temp=temp.next
print("After updating by value...")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("tail")