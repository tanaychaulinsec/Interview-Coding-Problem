class Tree:
    sum=0
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def GraterSum(root):
    if root.right:
        GraterSum(root.right)
    Tree.sum+=root.data
    root.data=Tree.sum
    if root.left:
        GraterSum(root.left)
    return root

def printTree(root):
    q = [root]
    res = []
    while q:
        n = q.pop(0)
        res.append(n.data)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    return res

    # def printInorder(root):
    #     if root:
    #         printInorder(root.left)
    #         print(root.data)
    #         printInorder(root.right)
root=Tree(4)
root.left = Tree(1)
root.right = Tree(6)
root.left.left = Tree(0)
root.left.right = Tree(2)
root.left.right.right = Tree(3)
root.right.left = Tree(5)
root.right.right = Tree(7)
root.right.right.right = Tree(8)
GraterSum(root)
print(printTree(root))
#printInorder(root)

