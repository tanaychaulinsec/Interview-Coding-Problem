class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Solution:
    def isSubTree(self,s,t):
        if s is None and t is None:
            return True
        if t is None:
            return True
        if s is None and t is not None:
            return  False
        return self.isEqual(s,t) or self.isSubTree(s.left,t) or self.isSubTree(s.right,t)

    def isEqual (self,s,t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return  False
        return s.val==t.val and self.isEqual(s.left,t.left) and self.isEqual(s.right,t.right)

if __name__=='__main__':
    s=TreeNode(2)
    s.left=TreeNode(3)
    s.right=TreeNode(4)
    s.left.right=TreeNode(2)
    s.right.right=TreeNode(5)
    s.left.left=TreeNode(1)
    t=TreeNode(4)
    t.right=TreeNode(5)
    tree=Solution()
    print(tree.isSubTree(s,t))


