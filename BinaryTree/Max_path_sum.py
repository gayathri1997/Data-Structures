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

def max_sum(root):
    if root==None:
        return 0
    else:
        return root.data + max(max_sum(root.left),max_sum(root.right))


root = Node(10,Node(8,Node(5),Node(3)),Node(30,Node(2),None))

inorder(root)
print(("\nMax sum"))
print(max_sum(root))