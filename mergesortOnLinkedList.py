class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Defining a class which will create our linked list and also defining other utility methods
class LinkedList:
    def __init__(self):
        self.head = None

# Defining the method to print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print (temp.data)
            temp = temp.next

# Defining the method to create a node at the end of the linked list
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

# Defining function which will merge two linked lists
def mergeLists(l1, l2):
    temp = None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.data <= l2.data:
        temp = l1
        temp.next = mergeLists(l1.next, l2)
    else:
        temp = l2
        temp.next = mergeLists(l1, l2.next)
    return temp

# Defining function which will sort the linked list using mergeSort
def mergeSort(head):
    if head is None or head.next is None:
        return head
    l1, l2 = divideLists(head)
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)
    head = mergeLists(l1, l2)
    return head
# Defining function which will divide a linked list into two equal linked lists
def divideLists(head):
    slow = head                     # slow is a pointer to reach the mid of linked list
    fast = head                     # fast is a pointer to reach the end of the linked list
    if fast:
        fast = fast.next
    while fast:
        fast = fast.next            # fast is incremented twice while slow is incremented once per loop
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return head, mid

# The main logic starts from here
if __name__ == '__main__':

    list1 = LinkedList()                    # Creating a linked list
    list1.append(20)                        # Assigning values to linked list in unsorted manner
    list1.append(10)
    list1.append(50)
    list1.append(40)
    list1.append(30)

    print ("Linked list before sorting")
    list1.printList()                       # Printing the unsorted linked list

    list1.head = mergeSort(list1.head)      # Applying mergeSort to linked list

    print ("Linked list after sorting")
    list1.printList()