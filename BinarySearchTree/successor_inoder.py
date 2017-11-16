class Node():
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def __repr__(self):
        return str(self.data)

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

def search(root,key,prev):
    if root is None or root.data == key:
        return root,prev
    if root.data < key:
        return search(root.right,key,root)
    else:
        return search(root.left,key,root)

def lefttMostOfSubtree(node):
    prev=None
    while node.left:
        print(node.data)
        prev=node
        node=node.left
    return node,prev


def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.data,end="   ")
    inorder(root.right)


def inorder_sucessor(root,node):
    s_node,s_prev=search(root,node,None)
    if s_node == None:
        print(s_prev.data)
    else:
        node,prev=lefttMostOfSubtree(s_node.right)
        print(node.data)

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
inorder(root)

inorder_sucessor(root,30)
