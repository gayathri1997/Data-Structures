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
    def del_right_node_greater(self):
        curr=self.head
        prev=None
        while curr.left:
            if curr.data < curr.left.data:
                if prev == None:
                    self.head=curr.left
                    curr=curr.left
                else:
                    prev.left=curr.left
                    curr=curr.left
            else:
                prev=curr
                curr=curr.left
        self.list_print()


sll=Singly_LinkedList()
sll.insert_at_end(12)
sll.insert_at_end(15)
sll.insert_at_end(10)
sll.insert_at_end(11)
sll.insert_at_end(5)
sll.insert_at_end(6)
sll.insert_at_end(2)
sll.insert_at_end(3)


print("lenght:",sll.length)
sll.list_print()
sll.del_right_node_greater()