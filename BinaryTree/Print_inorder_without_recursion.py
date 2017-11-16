def createStack():
    return []

def push(stack,data):
    stack.append(data)

def isEmpty(stack):
    return len(stack) == 0

def pop(stack):
    if isEmpty(stack):
        return "No elements"
    return stack.pop()


class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def print_without_recusion_preorder(root):
    stack=createStack()
    push(stack,root)
    while not isEmpty(stack):
        node=pop(stack)
        if node.right:
            push(stack,node.right)
        if node.left:
            push(stack,node.left)
        print(node.data)

def print_inorder_iteration(root):
    s=createStack()
    done=1
    current=root
    while done:
        if current:
            push(s,current)
            current=current.left
        else:
            if not isEmpty(s):
                current=pop(s)
                print(current.data)
                current=current.right
            else:
                done=0



root= Node(10,Node(8,Node(3),Node(5)),Node(2,Node(2),None))

print_inorder_iteration(root)