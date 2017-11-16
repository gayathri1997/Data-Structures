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
    def alternative_split(self):
        count=1
        curr=self.head
        even=Singly_LinkedList()
        odd=Singly_LinkedList()
        while curr:
            if count%2==1:
                odd.insert_at_end(curr.data)
            else:
                even.insert_at_end(curr.data)
            curr=curr.left
            count+=1
        print("Odd list :",end=" ")
        odd.list_print()
        print("Even list :",end=" ")
        even.list_print()


sll=Singly_LinkedList()
sll.insert_at_start(2)
sll.insert_at_start(1)
sll.insert_at_start(0)
sll.insert_at_end(3)
sll.insert_at_end(4)

print("lenght:",sll.length)
sll.list_print()
sll.alternative_split()