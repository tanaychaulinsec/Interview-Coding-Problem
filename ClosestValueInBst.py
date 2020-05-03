class TreeNode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
def dfs(root,target,min_Dif,minDifNode):
    if root==None:
        return
    if root.val==target:
        minDifNode[0]=target
    if min_Dif>abs(root.val-target):
        min_Dif=abs(root.val-target)
        minDifNode[0]=root.val
    if target>root.val:
        dfs(root.right,target,min_Dif,minDifNode)

    else:
        dfs(root.left, target, min_Dif, minDifNode)

def maxDiff(root,target):
    if root == None:
        return
    min_Dif=2**32
    minDifNode=[-1]
    dfs(root,target,min_Dif,minDifNode)
    return minDifNode
if __name__ == '__main__':
	root = TreeNode(9)
	root.left = TreeNode(4)
	root.right = TreeNode(17)
	root.left.left = TreeNode(3)
	root.left.right = TreeNode(6)
	root.left.right.left = TreeNode(5)
	root.left.right.right = TreeNode(7)
	root.right.right = TreeNode(22)
	root.right.right.left = TreeNode(20)
	target = 18
	print(maxDiff(root,target))