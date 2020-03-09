class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode
    def printlist(self):
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            else:
                print(currentNode.data)
                currentNode=currentNode.next

    def reverse(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
if __name__=='__main__' :
        llist1=Linkedlist()
        firstNode=Node(input("Enter 1st Node Data"))
        llist1.insert(firstNode)
        secondNode = Node(input("Enter 2nd Node Data"))
        llist1.insert(secondNode)
        thirdNode = Node(input("Enter 3rd Node Data"))
        llist1.insert(thirdNode)
        print("given Linked list",llist1.printlist())
        llist1.reverse()
        print("rev Linked list",llist1.printlist())
