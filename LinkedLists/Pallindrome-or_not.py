class Node:
    def __init__(self,data=None,left=None):
        self.data=data
        self.left=left

def isempty(s):
    return len(s)==0


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
    def print_middle(self):
        mid=self.length//2
        temp=0
        curr=self.head
        while temp<mid:
                curr=curr.left
                temp+=1
        return curr,mid
    def check_pallindrome_or_not(self):
        s=[]
        mid_node,mid=self.print_middle()
        curr=self.head
        temp=0
        while temp < mid:
            s.append(curr.data)
            curr=curr.left
            temp+=1
        print(s,mid_node.data,mid)
        if self.length%2==1:
            curr=mid_node.left
        else:
            curr=mid_node
        while curr != None and not isempty(s):
            a=s.pop()
            if a==curr.data:
                curr=curr.left
            else:
                return "Not pallindrome"
        return "Pallindrome"

sll=Singly_LinkedList()
sll.insert_at_start(30)
sll.insert_at_start(20)
sll.insert_at_start(10)
sll.insert_at_end(30)
sll.insert_at_end(20)
sll.insert_at_end(10)

sll.list_print()


print(sll.check_pallindrome_or_not())

