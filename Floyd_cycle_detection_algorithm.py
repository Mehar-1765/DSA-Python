# Floyd_cycle_detection_algorithm
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = None
tail = None
nodes=[]
n = int(input("Enter the size of SLL: "))
for i in range(n):
    value = int(input("Enter a value: "))
    newnode = node(value)
    nodes.append(newnode)
    if head is None:
        head = newnode
        tail = newnode
    else:
        tail.next = newnode
        tail = newnode
print("Original SLL:")        
temp = head
while temp:
    print(temp.data, end='->')
    temp = temp.next
print("tail")

pos=int(input('Enter position for cycle: '))
if pos>0:
    tail.next=nodes[pos-1]
slow=head
fast=head
cycle=False
while fast and fast.next:
    slow=slow.next
    fast=fast.next.next
    if slow==fast:
        cycle=True
        break
if cycle:
    print('Cycle detected')
    slow=head 
    while slow!=fast:
        slow=slow.next
        fast=fast.next
    start=slow
    print("Cycle starts at: ",start.data)
    print('Cycle path',end=' ')
    temp=start
    while True:
        print(temp.data,end='->')
        temp=temp.next
        if temp==start:
            break
    print(start.data)
else:
    print('No Cycle')