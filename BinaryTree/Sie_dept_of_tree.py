class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def get_size(root):
    if not root:
        return 0
    return (1+get_size(root.left)+get_size(root.right))

root = Node(10,Node(8,Node(3),Node(5)),Node(2,Node(22,Node(32)),None))

def get_dept(root):
    if not root:
        return 0
    return max(1+get_dept(root.left),1+get_dept(root.right))



print(get_size(root))
print(get_dept(root))
