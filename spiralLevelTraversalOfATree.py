class newNode:

    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Recursive Function to find height
# of binary tree
def height(root):
    if (root == None):
        return 0
    # Compute the height of each subtree
    lheight = height(root.left)
    rheight = height(root.right)

    # Return the maximum of two
    return max(lheight + 1, rheight + 1)

# Function to PrNodes from right to left
def rightToLeft(root, level):
    if (root == None):
        return
    if (level == 1):
        print(root.data,)
    elif (level > 1):
        rightToLeft(root.right, level - 1)
        rightToLeft(root.left, level - 1)
    # Function to PrNodes from left to right
def leftToRight(root, level):
    if (root == None):
        return
    if (level == 1):
        print(root.data)
    elif (level > 1):
        leftToRight(root.left, level - 1)
        leftToRight(root.right, level - 1)
    # Function to prReverse level order traversal
# of a Binary tree in spiral form
def reverseSpiral(root):
    # Flag is used to mark the
    # change in level
    flag = 1

    # Height of tree
    h = height(root)

    for i in range(h, 0, -1):

        # If flag value is one prNodes
        # from left to right
        if (flag == 1):
            leftToRight(root, i)
            # Mark flag as zero so that next time
            # tree is traversed from right to left
            flag = 0
        # If flag is zero prNodes
        # from right to left
        elif (flag == 0):
            rightToLeft(root, i)
            # Mark flag as one so that next time
            # Nodes are printed from left to right
            flag = 1
# Driver Code
if __name__ == '__main__':
    root = newNode(5)
    root.left = newNode(9)
    root.right = newNode(3)
    root.left.left = newNode(6)
    root.right.right = newNode(4)
    root.left.left.left = newNode(8)
    root.left.left.right = newNode(7)

    reverseSpiral(root)