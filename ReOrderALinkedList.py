from collections import deque
class Node:
    def __init__(self,data):
        self.data = data  # contains the data
        self.next = None  # contains the reference to the next node


# create a linked list without a cycle
class LinkedList:
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
        current =self.head
        while current is not None:
            print (current.data)
            current = current.next
    def reorder(self):
        if self.head is None:
            return self.head
        count=0
        curr=self.head
        while curr is not None:
            count+=1
            curr=curr.next
        stack=[]
        q=deque()
        mid=count//2
        curr=self.head
        for i in range(count):
            if i<mid:
                q.append(curr)
                curr=curr.next
            else:
                stack.append(Node(curr.data))
                curr=curr.next
        curr=self.head
        while len(stack) and len(q):
            stack_element = stack.pop()
            q_element = q.popleft()
            curr.next = q_element
            curr = curr.next
            curr.next = stack_element
            curr = curr.next
        if len(stack):
            stack_item=stack.pop()
            curr.next=stack_item
            curr=curr.next
            curr.next=None
        '''if not self.head:
            return self.head
        addres = []
        curr = self.head
        while curr:
            addres.append(curr)
            curr = curr.next
        addres = addres[:-int(len(addres) / 2) - 1:-1]
        curr = self.head
        for i in range(len(addres)):
            addres[i].next = curr.next
            curr.next = addres[i]
            curr = curr.next.next
            if i == len(addres) - 1:
                curr.next = None'''''



llist=LinkedList()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
llist.insert(5)
llist.printList()
llist.reorder()
llist.printList()


