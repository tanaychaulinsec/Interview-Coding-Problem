class TreeNode:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
def isValid(root):
	if not root:
		return True
	def dfs(root,MAX_INT,MIN_INT):
		if not root:
			return True
		if MIN_INT>=root.val or root.val>=MAX_INT:
			return  False
		left=right=True
		if root.left:
			left=dfs(root.left,root.val,MIN_INT)
		if root.right:
			right=dfs(root.right,MAX_INT,root.val)
		return left and right
	return dfs(root,2**32,-2**32)
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
	print(isValid(root))