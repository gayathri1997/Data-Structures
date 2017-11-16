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
    if (root1.data == root2.data) and check_identical(root1.left,root2.left) and check_identical(root1.right,root2.right):
        return True
    return False



root1=Node(10,Node(8,Node(3),Node(5)),Node(2,Node(2),None))
root2=Node(10,Node(8,Node(3),Node(5)),Node(2,Node(2)))

print(check_identical(root1,root2))