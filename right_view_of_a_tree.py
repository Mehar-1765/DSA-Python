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
print('Right view of the tree: ')
queue=deque([root])
while queue:
    size=len(queue)
    for i in range(size):
        node=queue.pop()
        if i==0:
            print(node.data,end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)