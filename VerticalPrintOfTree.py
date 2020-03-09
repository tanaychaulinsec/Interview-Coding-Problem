class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def verticalUtil(root,hd,m):
    if root is None:
        return
    try:
        m[hd].append(root.data)
    except:
        m[hd]=[root.data]
    verticalUtil(root.left,hd-1,m)
    verticalUtil(root.right,hd+1,m)

def printVerticalOrder(root):
    m=dict()
    hd=0
    verticalUtil(root,hd,m)
    for index, value in enumerate(sorted(m)):
        s=0
        for i in m[value]:
            s+=i
        print(s)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
print ("Vertical order traversal is")
printVerticalOrder(root)