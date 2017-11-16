class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def print_sum_leaf_root(root,parent,sum):
    if root is None:
        if sum==0:
            print(parent)
    else:
        parent.append(root.data)
        subsum=sum-root.data
        if root.left is None and root.right is None:
            print_sum_leaf_root(None,parent[:],subsum)
        if root.left:
            print_sum_leaf_root(root.left,parent[:],subsum)
        if root.right:
            print_sum_leaf_root(root.right,parent[:],subsum)



root=Node(10,Node(8,Node(3),Node(5)),Node(2,Node(2),None))

print_sum_leaf_root(root,[],14)
