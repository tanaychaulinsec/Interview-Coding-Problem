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
    return max(1+left,1+right)


def diameter(root):
    if root is None:
        return 0
    else:
        left_height=Height(root.left)
        right_height=Height(root.right)
        total_height=left_height+right_height+1
        left_diameter=diameter(root.left)
        right_diameter=diameter(root.right)
        max_diameter=max(left_diameter,right_diameter)
    return max(max_diameter,total_height)

if __name__ == '__main__':
    root = newNode(5)
    root.left = newNode(9)
    root.right = newNode(3)
    root.left.left = newNode(6)
    root.right.right = newNode(4)
    root.left.left.left = newNode(8)
    root.left.left.right = newNode(7)
    print (diameter(root))