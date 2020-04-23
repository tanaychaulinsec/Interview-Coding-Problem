class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist :
    def __init__(self):
        self.head=None
    def insert(self,newdata):
        newNode=Node(newdata)
        if self.head is None :
          self.head=newNode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                else:
                    lastnode=lastnode.next
            lastnode.next=newNode
    def printlist(self):
        currentNode=self.head
        while currentNode:
            print(currentNode.data)
            currentNode=currentNode.next
    def LinkedListPalindrome(self):
        rev=None
        slow=fast=self.head
        while fast and fast.next:
            fast=fast.next.next
            rev,rev.next,slow=slow,rev,slow.next
        if fast:
            slow=slow.next

        while rev and rev.data==slow.data:
            slow=slow.next
            rev=rev.next
        return not rev

llist = Linkedlist()
llist.insert(1)
llist.insert(2)
llist.insert(2)
llist.insert(1)
llist.printlist()
print(llist.LinkedListPalindrome())
