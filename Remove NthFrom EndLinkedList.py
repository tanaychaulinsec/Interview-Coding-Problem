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

    def removeNthFromEnd(self,head, n):
        slow = fast = self.head
        for i in range(n):
            fast = fast.next
        if (fast == None):
            return slow.next
        while (fast.next != None):
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

if __name__=='__main__' :
    n=int(input())
    llist=Linkedlist()
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    llist.insert(5)
    llist.printlist()
    llist.removeNthFromEnd(llist.head,n)
    llist.printlist()
