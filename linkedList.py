class Node :
    def __init__(self,data):
        self.data=data
        self.next=None
class linkList :
    def __init__(self):
        self.head=None
    def insert(self,newnode):
        if self.head=None :
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next=None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
if __name__=='__main__':
    llist=linkList()
    fst = Node(int(input()))
    llist.insert(fst)
    snd = Node(int(input()))
    llist.insert(snd)
    trd = Node(int(input()))
    llist.insert(trd)

