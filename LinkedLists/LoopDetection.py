class Node:
    def __init__(self,data=None,left=None):
        self.data=data
        self.left=left

class Singly_LinkedList:
    def __init__(self):
        self.head=None
        self.length=0
    def insert_at_start(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.left=self.head
            self.head=new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.left:
                curr=curr.left
            curr.left=new_node
    def insertNode_loop(self,data,loopplace):
        newnode = Node(data,next)
        curr=self.head
        while curr.left:
            curr=curr.left
        curr.left=newnode
        newnode.left=loopplace
    def detect_loop(self):
        slow=self.head
        fast=self.head.left
        while slow!=fast:
            if fast==None:
                print("No loops found")
                return None
            else:
                slow=slow.left
                if fast.left !=None:
                    fast=fast.left.left
                else:
                    fast=None
        print("Loop detected")
    def list_print(self):
        head=self.head
        while head.left:
            print(head.data,end=",")
            head=head.left
        print(head.data)


sll=Singly_LinkedList()
sll.insert_at_start(30)
sll.insert_at_start(20)
sll.insert_at_start(10)
sll.insert_at_end(40)
sll.detect_loop()
sll.insertNode_loop(50,sll.head.left)
sll.detect_loop()
#sll.list_print()