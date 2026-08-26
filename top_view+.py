from collections import deque
class node:
    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right=None
values=list(map(int,input("enter elements:").split()))
nodes=[]
for value in values:
    nodes.append(node(value))
    for i in range(len(nodes)):
        left=2*i+1
        right=2*i+2
        if left<len(nodes):
            nodes[i].left=nodes[left]
        if right<len(nodes):
            nodes[i].right=nodes[right]
root=nodes[0]
print('Top view of the tree: ')
queue=deque([(root,0)])
top={}
while queue:
    node,column=queue.popleft()
    if column not in top:
        top[column]=node.data
    if node.left:
        queue.append(node.left,column-1)
    if node.right:
        queue.append(node.right,column+1)
for column in sorted(top):
    print(top[column],end=' ')