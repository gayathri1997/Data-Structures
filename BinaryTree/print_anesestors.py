class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def get_anesestors(root,find):
    if root is None:
        return False
    if root.data == find:
        return True
    if get_anesestors(root.left,find) or get_anesestors(root.right,find):
        print(root.data)
        return True
    return False


root=Node(10,Node(8,Node(3),Node(5)),Node(2,Node(20),None))

get_anesestors(root,20)



