import queue
class newNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def LevelOrder(root):
    q = queue.Queue()
    res = []
    if root is None:
        return None
    q.put(root)
    while not q.empty():
        a = []
        size = q.qsize()
        while size != 0:
            curr = q.get()
            a.append(curr.data)
            if curr.left is not None:
                q.put(curr.left)
            if curr.right is not None:
                q.put(curr.right)
            size -= 1
        if len(a) != 0:
            res.append(a)
    return res

if __name__ == '__main__':
    root = newNode(5)
    root.left = newNode(9)
    root.right = newNode(3)
    root.left.left = newNode(6)
    root.right.right = newNode(4)
    root.left.left.left = newNode(8)
    root.left.left.right = newNode(7)
    print(LevelOrder(root))