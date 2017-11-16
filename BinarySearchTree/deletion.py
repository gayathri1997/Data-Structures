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

def rightMostOfSubtree(node):
    prev=None
    while node.right:
        prev=node
        node=node.right
    return node,prev

def DeleteNode(root,key):
    delNode,delNode_prev=search(root,key,None)
    rightmostnode,rightmostnode_prev=rightMostOfSubtree(delNode.left)
    print("deletion node:",delNode,delNode_prev)
    print("rightmose node:",rightmostnode,rightmostnode_prev)
    if rightmostnode.left is None:
        rightmostnode_prev.right=None
    else:
        rightmostnode_prev.right=rightmostnode.left
    if delNode_prev.data> rightmostnode.data:
        delNode_prev.left=rightmostnode
    else:
        delNode_prev.right=rightmostnode
    rightmostnode.left=delNode.left
    rightmostnode.right=delNode.right
    print("\n DELETE :",key,"---------------------------\n")
    inorder(root)



def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.data,end="   ")
    inorder(root.right)

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

DeleteNode(root,30)

