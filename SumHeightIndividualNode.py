class newNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def Height(root):
    if root is None:
        return 0
    else:
        left=Height(root.left)
        right=Height(root.right)
    return max((1+left),(1+right))


def HeightOfAllNode(root):
    if root is None:
        return 0
    return HeightOfAllNode(root.left)+Height(root)+HeightOfAllNode(root.right)


if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)

    print(HeightOfAllNode(root))
