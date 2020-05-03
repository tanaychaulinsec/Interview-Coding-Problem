from collections import OrderedDict
class LRUCache:
    def __init__(self,size):
        self.size=size
        self.cache = OrderedDict()
    def get(self, key):
        if self.cache.get(key):
            self.cache.move_to_end(key)  # Gotta keep this pair fresh, move to end of OrderedDict
            return self.cache[key]
        else:
            return -1

    def put(self,key, value):
        size=3
        if self.cache.get(key):
            self.cache.move_to_end(key)  # Gotta keep this pair fresh, move to end of OrderedDict
            self.cache[key] = value
        else:
            if len(self.cache) >= size:
                self.cache.popitem(last=False)  # last=True, LIFO; last=False, FIFO. We want to remove in FIFO fashion.
            self.cache[key] = value

LRUCache().put(1,1)
LRUCache().put(2,2)
print(LRUCache().get(1))      # returns 1
LRUCache().put(3, 3)   # evicts key 2
print(LRUCache().get(2))      # returns -1 (not found)
LRUCache().put(4, 4);    # evicts key 1
print(LRUCache().get(1))       # returns -1 (not found)
print(LRUCache().get(3))       # returns 3
print(LRUCache().get(4))


