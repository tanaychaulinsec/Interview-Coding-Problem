class Tree:
    sum=0
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def GraterSum(root,sum):
    if root :
        GraterSum(root.right,sum)
        sum+=root.data
        root.data=sum-root.data
        GraterSum(root.left,sum)
    else:
        print(sum)
    # def printInorder(root):
    #     if root:
    #         printInorder(root.left)
    #         print(root.data)
    #         printInorder(root.right)
root=Tree(11)
root.left = Tree(2)
root.right = Tree(29)
root.left.left = Tree(1)
root.left.right = Tree(7)
root.right.left = Tree(15)
root.right.right = Tree(40)
root.right.right.left = Tree(35)
GraterSum(root,Tree.sum)
#printInorder(root)

