def createQueue():
    queue=[]
    return queue

def isEmpty(queue):
    return len(queue) == 0


class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    inorder(root.left)
    inorder(root.right)

def print_level_wise(root):
    queue = createQueue()
    queue.append(root)
    while not isEmpty(queue):
        temp = queue.pop(0)
        print(temp.data,end=" ")
        if temp.left != None:
            queue.append(temp.left)
        if temp.right != None:
            queue.append(temp.right)


root = Node(1,Node(2,Node(3),Node(4)),Node(5))

inorder(root)
print(" ")
print_level_wise(root)