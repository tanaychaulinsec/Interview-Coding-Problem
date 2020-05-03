class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def dfs(pre,Min_INT,Max_INT):
    node=None
    if pre and Min_INT<pre[0]<Max_INT:
        node=TreeNode(pre[0])
        del pre[0]
        node.left=dfs(pre,Min_INT,node.val)
        node.right=dfs(pre,node.val,Max_INT)
    return TreeNode(node)
def Bst(pre):
    return str(dfs(pre,Min_INT=-2**32,Max_INT=2**32))
preorder=[8,5,1,7,10,12]
Bst(preorder)