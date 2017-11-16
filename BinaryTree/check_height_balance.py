class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def getHeight(root):
    if root is None:
        return 0
    else:
        return 1+ max(getHeight(root.left),getHeight(root.right))

def check_height_balanced(root):
    if abs(getHeight(root.left)-getHeight(root.right)) <=1:
        return True
    else:
        return False


root=Node(10,Node(8,Node(3),Node(5)),Node(2,Node(2),None))

print(check_height_balanced(root))