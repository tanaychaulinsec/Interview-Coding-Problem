class newnode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# function to check given sequence of root
# to leaf path exist in tree or not.
# index represents current element in
# sequence of rooth to leaf path
def existPath(root, arr, n, index):
    # If root is None, then there must
    # not be any element in array.
    if not root or index == n or arr[index] != root.data:
        return False
    if index == n - 1 and not (root.left or root.right):
        return True

    # If current node is equal to arr[index]
    # this means that till this level path
    # has been matched and remaining path
    # can be either in left subtree or
    # right subtree.
    return (existPath(root.left, arr, n, index + 1) or
             existPath(root.right, arr, n, index + 1))

# Driver Code
if __name__ == '__main__':

    # arr[] -. sequence of root to leaf path
    arr = [0,0,0,1]
    n = len(arr)
    root = newnode(0)
    root.left = newnode(1)
    root.right = newnode(0)
    root.left.left = newnode(0)
    root.left.right = newnode(1)
    root.left.right.left = newnode(0)
    root.left.right.right = newnode(1)
    root.left.left.right = newnode(1)
    root.right.left = newnode(0)
    root.right.right = newnode(0)
    print(existPath(root,arr,n,0))