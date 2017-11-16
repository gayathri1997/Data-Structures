class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class MyLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=None
    def insertNode(self,data):
        newnode = Node(data,None,None)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            head=self.head
            while head.next:
                head=head.next
            head.next=newnode
            newnode.prev=head
            self.tail=newnode
    def print_list(self):
        head=self.head
        while head.next:
            print(head.data,end=",")
            head=head.next
        print(head.data)
    def print_rev(self,head):
        if (head==None):
            return
        self.print_rev(head.next)
        print(head.data)



llist = MyLinkedlist()
llist.insertNode(10)
llist.insertNode(11)
llist.insertNode(12)
llist.insertNode(21)
llist.print_list()