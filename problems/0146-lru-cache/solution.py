class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # LRU
        self.left = Node(0,0)
        # MRU
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    # Delete node from Middle
    def remove(self,node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert on MRU
    def insert(self, node: Node):
        prev_node = self.right.prev
        next_node = self.right
        prev_node.next = next_node.prev = node
        node.next=next_node
        node.prev=prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove and insert in DLL
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove and insert in DLL
            self.remove(self.cache[key])
        self.cache[key] = Node(key=key, val=value)
        self.insert(self.cache[key])
        
        if len(self.cache)>self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
