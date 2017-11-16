class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left


vertical_dict={}

def vertical(root,level):
    if root is None:
        return None
    if level in vertical_dict.keys():
        vertical_dict[level].append(root.data)
    else:
        vertical_dict[level]=[root.data]
    vertical(root.left,level-1)
    vertical(root.right,level+1)

root=Node(1,Node(2,Node(4),Node(5)),Node(3,Node(6),Node(7)))

vertical(root,0)

print(vertical_dict)