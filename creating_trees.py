# Non-linear data structures
# Trees
# Node
# Edge

# 1.Proper Tree
# 2.Perfect Tree
# 3.Binary Tree
# 4.Skewed Tree
# 5.De-generative Tree
# 6.N-array Tree
# 7.Red black Tree

#creating tree
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
print("Root:",root.data)
print("Left:",root.left.data)
print("right:",root.right.data)
print("Left.left:",root.left.left.data)
print("Right.right:",root.left.right.data)