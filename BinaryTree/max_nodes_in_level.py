class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder(root):
    if root is None:
        return
    print(root.data)
    inorder(root.left)
    inorder(root.right)

root = Node(10,Node(8,Node(3),Node(5,Node(4,None,Node(2)))),Node(2,Node(2),Node(3)))

inorder(root)
