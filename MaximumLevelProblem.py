class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,data):
    if root==None:
        root=Node(data)
    elif root.data > data:
        root.left = insert(root.left, data)
    elif root.data < data:
        root.right = insert(root.right, data)
    return root
def maxLevelSum(root):
    if root is None:
        return 0
    res=root.data
    queue=[]
    queue.append(root)
    count=len(queue)
    while queue:
        temp=queue[0]





if __name__=='__main__':
    root=None
    root=insert(root,20)
    insert(root,10)
    insert(root,5)
    insert(root,15)
    insert(root,30)
    insert(root,25)
    insert(root,35)
    print(maxLevelSum(root))