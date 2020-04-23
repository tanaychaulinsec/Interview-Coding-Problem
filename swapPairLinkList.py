

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, newdata):
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                else:
                    lastnode = lastnode.next
            lastnode.next = newNode
    def swapPair(self):
        # fast=self.head
        # slow=self.head
        # while fast.next:
        #     fast=fast.next
        #     slow,fast=fast,slow
        #     if fast.next:
        #         fast=fast.next
        #         slow=fast
        prev =Node(0)
        prev.next = self.head
        head = prev
        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            c = prev.next.next.next
            prev.next = b
            prev.next.next = a
            prev.next.next.next = c
            prev = prev.next.next
        return head.next    



    def printlist(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next


if __name__ == '__main__':
    llist = Linkedlist()
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    llist.printlist()
    llist.swapPair()
    llist.printlist()


