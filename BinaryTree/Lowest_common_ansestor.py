class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def BST_Insert(root,node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                BST_Insert(root.left,node)
        elif root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                BST_Insert(root.right,node)

def LCA(root,node1,node2):
    ansestor=root.data
    if root.data > node1 and root.data > node2:
        return(LCA(root.left,node1,node2))
    elif root.data < node1 and root.data < node2:
        return(LCA(root.right,node1,node2))
    else: return ansestor

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

root = Node(10)
BST_Insert(root,Node(16))
BST_Insert(root,Node(5))
BST_Insert(root,Node(7))
BST_Insert(root,Node(12))
BST_Insert(root,Node(2))
BST_Insert(root,Node(15))
BST_Insert(root,Node(25))
BST_Insert(root,Node(11))
#inorder(root)
print(LCA(root,11,25))