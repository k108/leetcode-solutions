import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        Time Complexity : n * log( n )
        """
        heapq.heapify(nums)
        self.min_heap = nums
        self.k = k

        # If the heap is larger than k, 
        # remove the smallest elements until it has exactly k elements
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        

    def add(self, val: int) -> int:
        """
        Time Complexity : n * log( n )
        """
        heapq.heappush(self.min_heap, val)
        
        # If the heap is smaller than k or
        # If after adding the new value, the heap has more than k elements, 
        # pop the smallest
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # The smallest element in the heap is now the k-th largest element
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
