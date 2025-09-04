from collections import defaultdict

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        Time Complexity : O(n*log(n))
        Space Complexity : O(n)
        '''
        stops = defaultdict(int)
        for trip in trips:
            stops[trip[1]] += trip[0]
            stops[trip[2]] -= trip[0]
        
        for i in sorted(stops.keys()):
            capacity -= stops[i]
            if capacity < 0:
                break
        return capacity >= 0
