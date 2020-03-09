class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)
class ListNode:

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
    def __repr__(self):   #string in pintable representation
        return str(self.data)
def print_dll_from_head(node):
    if node is None:
        return
    while node.prev:
        node = node.prev
    while node:
        print(node.data,)
        node = node.next
def update_list_with_vertical_sum(root, list):
    if root is  None:
        return
    list.data = list.data +root.data
    if root.right is not None:
        if list.next is None:
            list.next = ListNode(0, list, None)
        update_list_with_vertical_sum(root.right, list.next)
    if root.left is not None:
        if list.prev is None:
            list.prev = ListNode(0, None, list)
        update_list_with_vertical_sum(root.left, list.prev)
def print_vertical_sum_binary_tree(root):
    list = ListNode(0, None, None)
    update_list_with_vertical_sum(root, list)
    print_dll_from_head(list)
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.right = Node(4)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    print_vertical_sum_binary_tree(root)
