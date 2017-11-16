class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def preorder(root):
    if not root:
        return None
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def postorder(root):
    if not root:
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.data)


root=Node(10,Node(8,Node(3),Node(5)),Node(2,Node(4),None))

preorder(root)