class Tree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def PrintPreorder(root):
    if root:
        print(root.data)
        PrintPreorder(root.left)
        PrintPreorder(root.right)
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
print("Preorder traversal of binary tree is")
PrintPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)