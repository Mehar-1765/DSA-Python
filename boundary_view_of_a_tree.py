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
print('Boundary view of the tree: ')
result=[]
result.append(root.data)
node=root.left
while node:
    if node.left or node.right:
        result.append(node.data)
    if node.left:
        node=node.left
    else:
        node=node.right
def addleaves(node):
    if node is None:
        return
    if node.left is None and node.right is None:
        result.append(node.data)
    addleaves(node.left)
    addleaves(node.right)
addleaves(root)
rightboundary=[]
node=root.right
while node:
    if node.left or node.right:
        rightboundary.append(node.data)
    if node.right:
        node=node.right
    else:
        node=node.left
rightboundary.reverse()
result.extend(rightboundary)
for column in result:
    print(column,end=' ')