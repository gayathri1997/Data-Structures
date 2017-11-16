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
    def swap_alternative(self,node,prev):
        if node == None:
            return None
        elif node.left == None:
            return None
        else:
            if prev==None:
                temp=node.left
                node.left=node.left.left
                self.head=temp
                temp.left=node
                self.swap_alternative(node.left,node)
            else:
                temp=node.left
                node.left=node.left.left
                temp.left=node
                prev.left=temp
                self.swap_alternative(node.left,node)



sll=Singly_LinkedList()
sll.insert_at_start(30)
sll.insert_at_start(20)
sll.insert_at_start(10)
sll.insert_at_end(40)
sll.insert_at_end(50)

print("lenght:",sll.length)
sll.list_print()
sll.swap_alternative(sll.head,None)
sll.list_print()