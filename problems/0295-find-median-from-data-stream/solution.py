class MaxHeap:
    def __init__(self):
        self.data = []

    def top(self):
        return -self.data[0]
        
    def push(self, val):
        return heapq.heappush(self.data, -val)
        
    def pop(self):
        return -heapq.heappop(self.data)
        
    def __getitem__(self, i): 
        return (-1)*self.data[i]
        
    def __len__(self): 
        return len(self.data)

class MinHeap:
    def __init__(self):
        self.data = []

    def top(self):
        return self.data[0]

    def push(self, val):
        return heapq.heappush(self.data, val)
        
    def pop(self):
        return heapq.heappop(self.data)
        
    def __getitem__(self, i): 
        return self.data[i]
        
    def __len__(self): 
        return len(self.data)

class MedianFinder:

    '''
    We have a max heap representing the sorted left half of the stream, and a min heap representing the sorted right half of the stream.
    The tops of these heaps represent the middle of the stream so far.
    
    To get the median:
        - if len(left) == len(right): return (left[0] + right[0]) / 2
        - elif len(left) > len(right): return left[0]
        - else: return right[0]
        
    To add a number x:
        If x <= left[0], add to left. Else, add to right.
        If abs(len(left) - len(right)) > 1: rebalance heaps.
        
    To rebalance:
        Pop an element from the bigger heap and add it to the smaller heap.
        
    Adding a number: O(log n) time, as there could be at most 2 pushes and 1 pop (log n).
    Finding the median: O(1), since we just look at the 0th elements of the heaps.
    Space: O(n), since we store every element in the heaps.
    '''

    def __init__(self):
        self.lower_max_heap = MaxHeap()
        self.upper_min_heap = MinHeap()

    def addNum(self, num: int) -> None:
        if len(self.lower_max_heap)==0 or num<self.lower_max_heap[0]:
            self.lower_max_heap.push(num)
        else:
            self.upper_min_heap.push(num)
        
        self.rebalance()

    def rebalance(self):
        if len(self.lower_max_heap)>len(self.upper_min_heap):
            bigger_heap = self.lower_max_heap
            smaller_heap = self.upper_min_heap
        else:
            bigger_heap = self.upper_min_heap
            smaller_heap = self.lower_max_heap

        if len(bigger_heap)-len(smaller_heap) >=2:
            smaller_heap.push(bigger_heap.pop())
        

    def findMedian(self) -> float:
        bigger_heap = None
        smaller_heap = None

        if len(self.lower_max_heap)>len(self.upper_min_heap):
            bigger_heap = self.lower_max_heap
            smaller_heap = self.upper_min_heap
        else:
            bigger_heap = self.upper_min_heap
            smaller_heap = self.lower_max_heap

        if len(bigger_heap)==len(smaller_heap):
            return (float(bigger_heap[0])+smaller_heap[0])/2
        else:
            return float(bigger_heap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
