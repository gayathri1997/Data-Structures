class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def count_leaf_nodes(root):
    if root is None:
        return 0
    elif root.right==None and root.left==None:
        return 1
    else:
        return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

root=root = Node(10,Node(8,Node(3),Node(5)),Node(2,Node(2),Node(20)))

print(count_leaf_nodes(root))