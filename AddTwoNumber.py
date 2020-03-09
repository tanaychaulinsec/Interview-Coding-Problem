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
            print(temp.data,end= "-> ")
            temp=temp.next
        print("Null")
    def sumOfTwoList(self,l1,l2):
        resNode=currNode=Node(0)
        carry=0
        while l1 or l2 or carry:
            if l1:
                carry+=l1.data
                l1=l1.next
            if l2:
                carry+=l2.data
                l2=l2.next

            currNode.next=Node(carry%10)
            currNode=currNode.next
            carry=carry//10
        return resNode.next

llist=LinkedList()
llist2=LinkedList()
llist.insert(2)
llist.insert(6)
llist.insert(4)
llist2.insert(4)
llist2.insert(5)
llist2.insert(3)
print("linked list 1")
llist.printlist()
print("linked list 2")
llist2.printlist()
res=LinkedList()
res.sumOfTwoList(llist.head,llist2.head)
print("linked list sum")
res.printlist()