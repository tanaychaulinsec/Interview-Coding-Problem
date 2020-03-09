class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,newdata):
        newNode=Node(newdata)
        if not self.head:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                else:
                    lastNode=lastNode.next
            lastNode.next=newNode
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
    def detectLoop(self):
        if self.head is None:
            return
        slow_p=self.head
        fast_p=self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p=slow_p.next
            fast_p=fast_p.next.next
            if slow_p==fast_p:
                print("Loop Found")
                return
llist=LinkedList()
llist.insert(10)
llist.insert(20)
llist.insert(30)
llist.insert(40)
llist.insert(50)
llist.head.next.next.next.next=llist.head
llist.detectLoop()



