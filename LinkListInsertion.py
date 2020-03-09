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


if __name__=='__main__' :
        # llist1=Linkedlist()
        # llist2=Linkedlist()
        # firstNode=Node(input("Enter 1st Node Data"))
        # llist1.insert(firstNode)
        # secondNode = Node(input("Enter 2nd Node Data"))
        # llist1.insert(secondNode)
        # thirdNode = Node(input("Enter 3rd Node Data"))
        # llist1.insert(thirdNode)
        llist=Linkedlist()
        llist.insert(1)
        llist.insert(2)
        llist.insert(3)
        llist.printlist()
