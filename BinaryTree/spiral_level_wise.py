class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def createStack():
    stack=[]
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack,item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack):
        return "No elements"
    return stack.pop()

def spiral_level_print(root):
    level=1
    odd=createStack()
    even=createStack()
    push(odd,root)
    while not isEmpty(odd) or not  isEmpty(even):
        while not isEmpty(odd):
            node=pop(odd)
            if node:
                print(node.data)
                push(even,node.right)
                push(even,node.left)
        while not isEmpty(even):
            node=pop(even)
            if node:
                print(node.data)
                push(odd,node.left)
                push(odd,node.right)

root=Node(1,Node(2,Node(7),Node(6)),Node(3,Node(5),Node(4)))
spiral_level_print(root)

