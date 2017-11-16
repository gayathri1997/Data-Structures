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

def inorder(root,min,max):
    if not root:
        return None
    inorder(root.left,min,max)
    if root.data> min and root.data< max:
        print(root.data)
    inorder(root.right,min,max)

root=Node(20)
root=Node(20)
insert(root,Node(30))
insert(root,Node(10))
insert(root,Node(15))
insert(root,Node(25))
insert(root,Node(35))
insert(root,Node(40))
insert(root,Node(29))
insert(root,Node(22))
insert(root,Node(8))
insert(root,Node(4))


inorder(root,8,30)