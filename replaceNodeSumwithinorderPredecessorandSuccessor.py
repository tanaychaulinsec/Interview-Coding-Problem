class getNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def replaceNodeWithSum(root,arr,i):
    if root is None:
        return
    replaceNodeWithSum(root.left,arr,i)
    root.data=arr[i[0]-1] + arr[i[0]+1]
    i[0]+=1
    replaceNodeWithSum(root.right,arr,i)

def inorderTraversal(root,arr):
    if root is None:
        return
    inorderTraversal(root.left,arr)
    arr.append(root.data)
    inorderTraversal(root.right,arr)
def replaceNodeWithSumUtil(root):
    if root is None:
        return
    arr=[]
    arr.append(0)
    inorderTraversal(root,arr)
    arr.append(0)
    i=[1]
    replaceNodeWithSum(root,arr,i)

def preorderTraversal(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorderTraversal(root.left)
    preorderTraversal(root.right)

root = getNode(1)
root.left = getNode(2)
root.right = getNode(3)
root.left.left = getNode(4)
root.left.right = getNode(5)
root.right.left = getNode(6)
root.right.right = getNode(7)

print("Preorder Traversal before",
      "tree modification:")
preorderTraversal(root)

replaceNodeWithSumUtil(root)
print()
print("Preorder Traversal after",
      "tree modification:")
preorderTraversal(root)