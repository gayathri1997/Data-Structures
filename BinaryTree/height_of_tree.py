class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder(root):
    if root is None:
        return
    print(root.data,end=",")
    inorder(root.left)
    inorder(root.right)

def preorder(root):
    if root is None:
        return
    preorder(root.left)
    print(root.data,end=",")
    preorder(root.right)


def maxDepth(root):
    if root == None:
        return 0
    else:
        lDepth = maxDepth(root.left)
        rDepth = maxDepth(root.right)
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1


root = Node(1,Node(2,Node(3),Node(4)),Node(5))

inorder(root)
print(" ")
preorder(root)
print(" ")
print("Height of tree:",maxDepth(root))