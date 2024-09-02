import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]= -1 * stones[i]
        heapq.heapify(stones)
        while len(stones)>1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            diff = abs(x-y)
            if diff > 0:
                heapq.heappush(stones, -1 * diff)
                
        if stones:
            return -1 * stones[0]
        else:
            return 0




        
