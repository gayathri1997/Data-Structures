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
    def comman_in_lists(self,sll2):
        l1=self.head
        l2=sll2.head
        while l1 != None and l2 != None:
            if l1.data == l2.data:
                print(l1.data)
                l1=l1.left
                l2=l2.left
            elif l1.data<l2.data:
                l1=l1.left
            else:
                l2=l2.left

sll1=Singly_LinkedList()
sll1.insert_at_start(30)
sll1.insert_at_start(20)
sll1.insert_at_start(10)
sll1.insert_at_end(40)

sll2=Singly_LinkedList()
sll2.insert_at_end(10)
sll2.insert_at_end(20)
sll2.insert_at_end(23)
sll2.insert_at_end(23)
sll2.insert_at_end(33)
sll2.insert_at_end(40)

print("lenght:",sll1.length)
sll1.list_print()
print("lenght:",sll2.length)
sll2.list_print()
sll1.comman_in_lists(sll2)