class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def construct_tree_preoder_inorder(preorder,inorder,start,end):
    if start > end:
        return None
    current=Node(preorder.pop(0))
    node_index=inorder.index(current.data)
    if start == end:
        return current
    current.left=construct_tree_preoder_inorder(preorder,inorder,start,node_index-1)
    current.right=construct_tree_preoder_inorder(preorder,inorder,node_index+1,end)
    return current


def Printpreorder(root):
    if not root:
        return None
    print(root.data)
    preorder(root.left)
    preorder(root.right)


preorder=[10,8,3,5,2,4]
inorder=[3,8,5,10,4,2]

root=construct_tree_preoder_inorder(preorder,inorder,0,len(inorder)-1)

pr