class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def printLeaves(root):
    if (root) :
        printLeaves(root.left)
        if root.left is None and root.right is None:
            print(root.data),
        printLeaves(root.right)
def printBoundaryLeft(root):
    if (root):
        if (root.left):
            print(root.data)
            printBoundaryLeft(root.left)
        elif (root.right):
            print(root.data)
            printBoundaryLeft(root.right)
def printBoundaryRight(root):
    if (root):
        if (root.right):
            printBoundaryRight(root.right)
            print(root.data)
        elif (root.left):
            printBoundaryRight(root.left)
            print(root.data)
def printBoundary(root):
    if (root):
        print(root.data)
        printBoundaryLeft(root.left)
        printLeaves(root.left)
        printLeaves(root.right)
        printBoundaryRight(root.right)
root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.left.right = Node(5)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
printBoundary(root)
