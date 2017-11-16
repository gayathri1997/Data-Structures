class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class MyLinkedlist:
    length=0
    def __init__(self):
        self.head=None
    def insertNode(self,data):
        MyLinkedlist.length+=1
        newnode = Node(data,None)
        if self.head is None:
            self.head = newnode
        else:
            head=self.head
            while head.next:
                head=head.next
            head.next=newnode
    def insert_list_at_end(self,interset):
        MyLinkedlist.length+=1
        head=self.head
        while head.next != None:
            head=head.next
        head.next= interset
    def print_list(self):
        head=self.head
        while head.next:
            print(head.data,end=",")
            head=head.next
        print(head.data)

def intersection(list1,list2):
    l1=list1.length
    l2=list2.length
    if l2>l1:
        curr=list1.head
    else:
        curr=list2.head
    i=0
    print(curr.data)
    while i>abs(l1-l2)+1:
        curr=curr.next
    print(curr.data)

llist1 = MyLinkedlist()
llist2 = MyLinkedlist()
interset=Node(10,Node(20,Node(30)))
llist1.insertNode(1)
llist1.insertNode(2)
llist1.insert_list_at_end(interset)
llist1.print_list()
llist2.insertNode(11)
#llist2.insertNode(22)
llist2.insert_list_at_end(interset)
llist2.print_list()


intersection(llist1,llist2)