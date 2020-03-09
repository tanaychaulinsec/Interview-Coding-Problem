class Node:
    def __init__(self,data):
        self.data=data
        self.left=  None
        self.right=None
def insert(root,data):
       if root==None:
           root=Node(data)
       elif root.data>data:
           root.left=insert(root.left,data)
       elif root.data <data:
           root.right=insert(root.right,data)
       return root
def distanceFrom(root,x):
    if root.data==x:
        return 0
    elif root.data>x:
        return 1+ distanceFrom(root.left,x)

    return 1+distanceFrom(root.right,x)

def distanceBetween(root,a,b):
    if root==None:
        return 0

    elif root.data>a and root.data>b:
        return  distanceBetween(root.left,a,b)

    elif root.data<a and root.data<b:
        return distanceBetween(root.right,a,b)

    elif a<=root.data<=b:
        return (distanceFrom(root,a)+
                distanceFrom(root,b))

def findDistance(root,a,b):
    if a>b:
        a,b=b,a
    return distanceBetween(root,a,b)


if __name__=='__main__':
    root=None
    root=insert(root,20)
    insert(root,10)
    insert(root,5)
    insert(root,15)
    insert(root,30)
    insert(root,25)
    insert(root,35)
    print(findDistance(root,5,35))
