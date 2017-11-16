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


def Merge_lists(list1,list2):
    list3=Singly_LinkedList()
    cur1=list1.head
    cur2=list2.head
    while cur1 or cur2:
        if cur1 and cur2:
            if cur1.data < cur2.data:
                list3.insert_at_end(cur1.data)
                cur1=cur1.left
            else:
                list3.insert_at_end(cur2.data)
                cur2=cur2.left
            continue
        if cur1 is None:
            list3.insert_at_end(cur2.data)
            cur2=cur2.left
            continue
        if cur2 is None:
            list3.insert_at_end(cur1.data)
            cur2=cur1.left
    return list3


s1=Singly_LinkedList()
s1.insert_at_start(30)
s1.insert_at_start(20)
s1.insert_at_start(10)

s2=Singly_LinkedList()
s2.insert_at_start(32)
s2.insert_at_start(22)
s2.insert_at_start(12)
print("List 1:")
s1.list_print()
print("List 2:")
s2.list_print()
s3=Merge_lists(s1,s2)
s3.list_print()
