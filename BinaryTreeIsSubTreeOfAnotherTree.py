class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Solution:
    def isSubTree(self,root,t):
        if root is None and t is None:
            return True
        if t is None:
            return True
        if root is None and t is not None:
            return  False
        return self.isEqual(root,t) or self.isSubTree(root.left,t) or self.isSubTree(root.right,t)

    def isEqual (self,root,t):
        if root is None and t is None:
            return True
        if root is None or t is None:
            return  False
        return root.val==t.val and self.isEqual(root.left,t.left) and self.isEqual(root.right,t.right)

if __name__=='__main__':
    root=TreeNode(2)
    root.left=TreeNode(3)
    root.right=TreeNode(4)
    root.left.right=TreeNode(2)
    root.right.right=TreeNode(5)
    root.left.left=TreeNode(1)
    t=TreeNode(4)
    t.right=TreeNode(5)
    tree=Solution()
    print(tree.isSubTree(root,t))


