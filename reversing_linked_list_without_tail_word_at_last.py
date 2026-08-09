class node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = None
tail = None
n = int(input("Enter the size of SLL: "))
for i in range(n):
    value = int(input("Enter a value: "))
    newnode = node(value)
    if head is None:
        head = newnode
        tail = newnode
    else:
        tail.next = newnode
        tail = newnode
print("Original SLL:")        
temp = head
while temp.next:
    print(temp.data, end='->')
    temp = temp.next
print(temp.data)
#reverse the sll
prev = None
current = head
while current:
    next = current.next
    current.next = prev
    prev = current
    current = next
head = prev
print("Reversed SLL:")
temp = head
while temp.next:
    print(temp.data, end='->')
    temp = temp.next
print(temp.data)