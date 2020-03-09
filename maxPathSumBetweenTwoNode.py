class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,data):
    if root is None:
        root=Node(data)
    elif root.data<data:
        root.left=insert(root.left,data)
    elif root.data>data:
        root.right=insert(root.right,data)
    return root
def leveordersumUtil(root,res):
    if root is None:
        return
    if root.left is None and root.right is None:
        return root.data
    ls=leveordersumUtil(root.left,res)
    rs=leveordersumUtil(root.right,res)

    if root.left is not None and root.right is not None:
        res[0]=max(res[0],ls+rs+root.data)
        return max(ls+root.data,rs+root.data)
    if root.left is None:
        return rs+root.data
    if root.right is None:
        return ls+root.data
def levelordersum(root):
    res=[0]
    leveordersumUtil(root,res)
    return res[0]
root=None
root=insert(root,10)
insert(root,8)
insert(root,6)
insert(root,7)
insert(root,4)
insert(root,13)
insert(root,14)
insert(root,18)
insert(root,16)
print(levelordersum(root))


