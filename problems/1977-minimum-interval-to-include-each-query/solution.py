import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
        Time Complexity : O(n log n + m log m)
        Space Complexity : O(n + m)
        '''
        '''
        Approach :
        - sort intervals by size
        - sort queries
        - for each query, if interval_left <= query,
        add to min-heap (interval_size, interval_right),
        here interval_right will be our tie-breaker
        then keep popping invalid intervals with query > interval_right
        else add that interval_size to answer
        '''
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
