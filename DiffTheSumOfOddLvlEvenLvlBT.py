class newNode:

    # Construct to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# return difference of sums of odd
# level and even level
def evenOddLevelDifference(root):
    if (not root):
        return 0

    # create a queue for
    # level order traversal
    q = []
    q.append(root)

    level = 0
    evenSum = 0
    oddSum = 0

    # traverse until the queue is empty
    while (len(q)):

        size = len(q)
        level += 1

        # traverse for complete level
        while (size > 0):

            temp = q[0]  # .front()
            q.pop(0)

            # check if level no. is even or
            # odd and accordingly update
            # the evenSum or oddSum
            if (level % 2 == 0):
                evenSum += temp.data
            else:
                oddSum += temp.data

                # check for left child
            if (temp.left):
                q.append(temp.left)

                # check for right child
            if (temp.right):
                q.append(temp.right)

            size -= 1

    return (oddSum - evenSum)


# Driver Code
if __name__ == '__main__':
    """  
    Let us create Binary Tree shown 
    in above example """
    root = newNode(5)
    root.left = newNode(2)
    root.right = newNode(6)
    root.left.left = newNode(1)
    root.left.right = newNode(4)
    root.left.right.left = newNode(3)
    root.right.right = newNode(8)
    root.right.right.right = newNode(9)
    root.right.right.left = newNode(7)

    result = evenOddLevelDifference(root)
    print("Diffence between sums is", result)