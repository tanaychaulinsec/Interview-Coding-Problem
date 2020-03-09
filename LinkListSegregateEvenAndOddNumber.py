class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkList:
    def __init__(self):
        self.head=None
    def insert(self,newdata):
        newNode=Node(newdata)
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                else:
                    lastNode=lastNode.next
            lastNode.next=newNode
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
    def segrigateOddEven(self):
        OddHead=None
        EvenHead=None
        OddLast=None
        EvenLast=None
        curr=self.head
        while curr is not None:
            if curr.data%2==0:
                if EvenHead is None:
                    EvenHead=EvenLast=curr
                else:
                    EvenLast.next=curr
                    EvenLast=curr
            else:
                if OddHead is None:
                    OddHead=OddLast=curr
                else:
                    OddLast.next=curr
                    OddLast=curr
            curr=curr.next
        if EvenHead is not None:
            self.head=EvenHead
        if EvenLast is not None:
            EvenLast.next=OddHead
        if OddLast is not None:
            OddLast.next=None
llist=LinkList()
llist.insert(1)
llist.insert(2)
llist.insert(4)
llist.insert(3)
llist.insert(6)
llist.insert(8)
llist.printList()
llist.segrigateOddEven()
llist.printList()
