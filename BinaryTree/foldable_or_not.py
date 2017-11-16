class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left


def check_identical(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None and root2 is not Node: return False
    if root2 is None and root1 is not Node: return False
    if check_identical(root1.left,root2.left) and check_identical(root1.right,root2.right):
        return True
    return False

def foldable_or_not(root):
    if check_identical(root.left,root.right):
        return True
    return False



root=Node(10,Node(8,Node(3)),Node(2,Node(4),Node(20)))

print("check foldable:",foldable_or_not(root))