class Node():
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def insert(root,node):
    if root.data > node.data:
            if root.left:
                insert(root.left,node)
            else:
                root.left=node
    elif root.data < node.data:
            if root.right:
                insert(root.right,node)
            else:
                root.right=node
    else:
        print("Duplicate Cannot insert the node:",node.data)
        return None

def isBST(node):
    if node==None:
        return True
    if node.left!=None and node.left.data > node.data:
        return False
    if node.right!=None and node.right.data < node.data:
        return False
    if (not isBST(node.left)) or (not isBST(node.right)):
        return False
    return True



def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.data)
    inorder(root.right)

root=Node(20)
insert(root,Node(30))
insert(root,Node(10))
insert(root,Node(15))
insert(root,Node(25))
insert(root,Node(35))
inorder(root)

print("IS BST: ",isBST(root))