class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class MyLinkedlist:
    def __init__(self):
        self.head=None
        self.length=None
    def insertNode(self,data):
        newnode = Node(data,None)
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
    def insertNode_loop(self,data,next):
        newnode = Node(data,next)
        head=self.head
        while head.next:
            head=head.next
        head.next=newnode
    def detect_loop(self):
        slow=self.head.next
        fast=self.head.next.next
        while slow!=fast:
            if fast == None:
                return "No loops"
            else:
                slow=slow.next
                fast=fast.next.next
        return "Loop detected",fast
    def remove_loop(self,fast):
        slow=self.head
        while slow.next!=fast.next:
            slow=slow.next
            fast=fast.next
        print("loop ended at:",fast.data)
        fast.next=None
        self.print_list()


llist = MyLinkedlist()
llist.insertNode(10)
llist.insertNode(20)
llist.insertNode(30)
llist.insertNode(40)
llist.insertNode(50)
llist.print_list()
llist.insertNode_loop(60,llist.head.next.next)
op,fast=llist.detect_loop()
print(op,fast.data)
llist.remove_loop(fast)