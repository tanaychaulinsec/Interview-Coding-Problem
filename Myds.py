import random
# Class to represent the required
# data structure
class MyDS:

    # Constructor (creates a list and a hash)
    def __init__(self):
        # A resizable array
        self.arr = []
        # A hash where keys are lists elements
        # and values are indexes of the list
        self.hashd = {}
        # A Theta(1) function to add an element
    # to MyDS data structure
    def add(self, x):
        # If element is already present,
        # then nothing has to be done
        if x in self.hashd:
            return

        # Else put element at
        # the end of the list
        s = len(self.arr)
        self.arr.append(x)

        # Also put it into hash
        self.hashd[x] = s

        # A Theta(1) function to remove an element

    # from MyDS data structure
    def remove(self, x):
        # Check if element is present
        index = self.hashd.get(x, None)
        if index == None:
            return

        # If present, then remove
        # element from hash
        del self.hashd[x]

        # Swap element with last element
        # so that removal from the list
        # can be done in O(1) time
        size = len(self.arr)
        last = self.arr[size - 1]
        self.arr[index], \
        self.arr[size - 1] = self.arr[size - 1], \
                             self.arr[index]
        # Remove last element (This is O(1))
        del self.arr[-1]

        # Update hash table for
        # new index of last element
        self.hashd[last] = index

    def getRandom(self):

        # Find a random index from 0 to size - 1
        index = random.randrange(0, len(self.arr))

        # Return element at randomly picked index
        return self.arr[index]

        # Returns index of element

    # if element is present,
    # otherwise none
    def search(self, x):
        return self.hashd.get(x, None)
    # Driver Code
if __name__ == "__main__":
    ds = MyDS()
    ds.add(10)
    ds.add(20)
    ds.add(30)
    ds.add(40)
    print(ds.search(30))
    ds.remove(20)
    ds.add(50)
    print(ds.search(50))
    print(ds.getRandom())