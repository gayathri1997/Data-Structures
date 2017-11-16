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

def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def leastCommonAnsestor(root,node1,node2):
    if root==None:
        return "Nothing is common"
    elif root.data > node1 and root.data > node2:
        leastCommonAnsestor(root.left,node1,node2)
    elif root.data < node1 and root.data < node2:
        leastCommonAnsestor(root.right,node1,node2)
    else:
        print("Common node is:",root.data)

root=Node(20)
insert(root,Node(30))
insert(root,Node(10))
insert(root,Node(15))
insert(root,Node(25))
insert(root,Node(35))
insert(root,Node(40))
insert(root,Node(22))
insert(root,Node(29))
inorder(root)

leastCommonAnsestor(root,22,29)