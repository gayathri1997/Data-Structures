class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left
def preorder(root):
    if not root:
        return None
    print(root.data)
    preorder(root.left)
    preorder(root.right)


def double_tree(root):
    if not root:
        return None
    new_node=Node(root.data,Node(root.data),None)
    current=new_node.left
    current.left=double_tree(root.left)
    current.right=double_tree(root.right)
    return new_node


root=Node(1,Node(2),Node(3))

new_root=double_tree(root)

preorder(new_root)