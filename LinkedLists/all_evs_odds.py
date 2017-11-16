class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class MyLinkedlist:
    def __init__(self):
        self.head=None
        self.length=0
    def insertNode(self,data):
        newnode = Node(data,None)
        self.length=self.length+1
        if self.head is None:
            self.head = newnode
        else:
            head=self.head
            while head.next:
                head=head.next
            head.next=newnode
    def print_list(self):
        head=self.head
        while head.next:
            print(head.data,end=",")
            head=head.next
        print(head.data)
    def del_position(self,pos):
        count=1
        head=self.head
        while count+1 < pos:
            count=count+1
            head=head.next
        head.next = head.next.next
    def reverseList(self):
        prev=None
        remain=None
        head=self.head
        while(head != None):
            remain=head.next
            head.next = prev
            prev=head
            head=remain
        self.head=prev


llist = MyLinkedlist()
llist.insertNode(1)
llist.insertNode(2)
llist.insertNode(3)
llist.insertNode(4)
llist.insertNode(5)
llist.print_list()

