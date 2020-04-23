from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def bstFromPreorder( preorder):
    def bst(pre, min, max):
        node = None
        if pre and min < pre[0] < max:
            node = TreeNode(pre[0])
            del pre[0]
            node.left = bst(pre, min, node.val)
            node.right = bst(pre, node.val, max)
        return TreeNode(node)

    return bst(preorder, -2**32, 2**32)

preorder=[8,5,1,7,10,12]
print(bstFromPreorder(preorder))