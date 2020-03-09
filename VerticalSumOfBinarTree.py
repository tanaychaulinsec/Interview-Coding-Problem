from collections import defaultdict
class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    def vertical_traverse(self, level):
        stack = []
        result = defaultdict(list) # key: level, value: list of node identifier
        stack.append((self,level))
        while len(stack) > 0:
            node, level = stack.pop(-1)
            result[level].append(node.value)
            if node.left is not None:
                stack.append((node.left, level-1))
            if node.right is not  None:
                stack.append((node.right, level+1))
        return result

if __name__ == "__main__":
    root =TreeNode(1,TreeNode(2,TreeNode(4,None,None),TreeNode(5,None,None)),TreeNode(3,TreeNode(6,None,None),TreeNode(7,None,None)))
    #root=TreeNode(1,TreeNode(2,None,None)),TreeNode(3,TreeNode(5,TreeNode(7,None,None),TreeNode(8,None,None)),TreeNode(6,None,None))
    result = root.vertical_traverse(0)
    for k,v in result.items():
        print (k, sum(v))