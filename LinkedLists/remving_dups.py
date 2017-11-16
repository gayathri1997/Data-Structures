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
    def remove_node(self,prev,node):
        prev.left=node.left
    def remove_dups(self):
        dic={}
        prev=None
        curr=self.head
        while curr:
                if curr.data in dic.keys():
                    self.remove_node(prev,curr)
                    curr=curr.left
                    continue
                else:
                    dic[curr.data]=0
                prev=curr
                curr=curr.left

sll=Singly_LinkedList()
sll.insert_at_start(30)
sll.insert_at_start(20)
sll.insert_at_start(10)
sll.insert_at_end(40)
sll.insert_at_end(30)
sll.insert_at_end(10)
sll.insert_at_end(20)

print("lenght:",sll.length)
sll.list_print()
sll.remove_dups()
sll.list_print()

