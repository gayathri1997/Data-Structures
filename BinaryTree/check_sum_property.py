class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def check_sum_property(root):
    lsum=0;rsum=0
    if root==None or (root.left == None and root.right==None):
            return True
    else:
        if root.left != None:
            lsum = root.left.data
        if root.right != None:
            rsum = root.right.data
        if (root.data == lsum+rsum) and check_sum_property(root.left) and check_sum_property(root.right):
            return True
        else:
            return False

root= Node(10,Node(8,Node(3),Node(5)),Node(2,Node(2),None))

print(check_sum_property(root))