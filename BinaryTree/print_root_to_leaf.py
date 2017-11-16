class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def print_root_leaf(root,parent):
    if root is None:
        print(parent)
    else:
        parent.append(root.data)
        if root.left is None and root.right is None:
            print_root_leaf(None,parent)
        else:
            if root.left:
                print_root_leaf(root.left,parent[:])
            if root.right:
                print_root_leaf(root.right,parent[:])

root= Node(10,Node(8,Node(3),Node(5)),Node(2,Node(2),None))

print_root_leaf(root,[])