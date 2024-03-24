class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # map key to node
        self.cache = {}
        # left => LRU, right => MRU
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    # remove node from list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    # insert node at right
    def insert(self, node):
        prev_node = self.right.prev
        next_node = self.right
        prev_node.next = next_node.prev = node
        node.next, node.prev = next_node, prev_node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove LRU from doubly linked list and remove LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
