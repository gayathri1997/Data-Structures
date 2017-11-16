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

def get_height(root):
    if root == None:
        return 0
    return max(get_height(root.left),get_height(root.right))+1

def check_balanced_height(root):
    if abs(get_height(root.left)-get_height(root.right)) <= 1:
        return True


root = Node(10,Node(8,Node(3),Node(5,Node(4,None,Node(2)))),Node(2,Node(2),Node(3)))

inorder(root)
print("Height:",get_height(root))

if check_balanced_height(root):
    print("Balanced")
else:
    print("Unbalanced")