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
        self.length+=1
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.left:
                curr=curr.left
            curr.left=new_node
        self.length+=1
    def list_print(self):
        head=self.head
        while head.left:
            print(head.data,end=",")
            head=head.left
        print(head.data)
    def sort_012(self):
        count=0
        prev=self.head
        curr=prev.left
        llen=self.length
        while count < llen :
            count+=1
            if curr.data==0:
                prev.left=curr.left
                self.insert_at_start(curr.data)
                curr=curr.left
            elif curr.data==1:
                prev=curr
                curr=curr.left
            elif curr.data==2:
                prev.left=curr.left
                self.insert_at_end(curr.data)
                curr=curr.left
        self.list_print()


sll=Singly_LinkedList()
sll.insert_at_end(1)
sll.insert_at_end(0)
sll.insert_at_end(2)
sll.insert_at_end(1)
sll.insert_at_end(0)
sll.insert_at_end(2)
sll.insert_at_end(1)
sll.insert_at_end(0)

print("lenght:",sll.length)
sll.list_print()
sll.sort_012()