class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def height(root):
    if root is None:
        return 0
    return (1+max(height(root.left),height(root.right)))

def daimeter(root):
    if root is None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    rd=daimeter(root.right)
    ld=daimeter(root.left)
    return max(lh+rh+1,max(ld,rd))



root=Node(10,Node(8,Node(3),Node(5)),Node(2,Node(4,Node(23)),None))

print(daimeter(root))