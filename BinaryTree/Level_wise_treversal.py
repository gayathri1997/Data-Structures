def push(stack,data):
    stack.append(data)

def pop(stack):
    return stack.pop(0)

def isStackEmpty(stack):
    return True if len(stack)==0 else False

class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def print_level_wise(root):
    stack=[]
    push(stack,root)
    while not isStackEmpty(stack):
        node=pop(stack)
        print(node.data)
        if node.left:
            push(stack,node.left)
        if node.right:
            push(stack,node.right)

root = Node(10,Node(8,Node(3),Node(5)),Node(2,Node(22),None))

print_level_wise(root)
