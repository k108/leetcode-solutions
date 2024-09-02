import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            # square root takes time
            min_heap.append((point[0]*point[0] + point[1]*point[1], point))

        heapq.heapify(min_heap)

        return [heapq.heappop(min_heap)[1] for i in range(k)]

        
