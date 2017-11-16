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

temp=[]

def inorder(root):
    if not root:
        return None
    inorder(root.left)
    temp.append(root.data)
    inorder(root.right)


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
print("Kth node is :",temp[0])