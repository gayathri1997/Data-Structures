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

def print_ansetors(root,node,ansetors):
    #print(root,node)
    if root == None:
        return
    elif root.data == node:
        print(ansetors)
    elif root.left == None and root.right == None:
        return
    else:
        ansetors.append(root.data)
        print_ansetors(root.left,node,ansetors[:])
        print_ansetors(root.right,node,ansetors[:])


root = Node(10,Node(8,Node(3),Node(5)),Node(2,Node(7),None))

inorder(root)

print("\nAnesestors")
print_ansetors(root,7,[])

