class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

root = Node(10,Node(8,Node(3),Node(5)),Node(2,Node(22,Node(32)),None))

def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def mirror_tree(root):
    if not root:
        return None
    else:
        mirror_tree(root.left)
        mirror_tree(root.right)
        root.left,root.right=root.right,root.left

inorder(root)
print()
mirror_tree(root)
print("Mirror")
inorder(root)