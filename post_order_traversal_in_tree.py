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
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=' ')
postorder(root)